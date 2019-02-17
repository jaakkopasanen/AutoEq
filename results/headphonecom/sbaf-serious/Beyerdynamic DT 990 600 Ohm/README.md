# Beyerdynamic DT 990 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.1; 31 -2.7; 34 -3.2; 37 -3.6; 41 -4.2; 45 -4.7; 49 -5.1; 54 -5.7; 60 -6.4; 66 -6.8; 72 -6.6; 79 -6.8; 87 -8.5; 96 -9.4; 106 -10.1; 116 -10.6; 128 -11.0; 141 -11.4; 155 -11.8; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.6; 249 -11.4; 274 -11.0; 302 -10.5; 332 -9.8; 365 -8.9; 402 -8.2; 442 -7.4; 486 -7.1; 535 -6.4; 588 -6.0; 647 -5.6; 712 -5.2; 783 -4.9; 861 -4.9; 947 -5.4; 1042 -5.6; 1146 -6.0; 1261 -6.0; 1387 -6.3; 1526 -6.5; 1678 -6.6; 1846 -6.9; 2031 -6.5; 2234 -5.1; 2457 -4.3; 2703 -4.3; 2973 -5.1; 3270 -5.4; 3597 -5.1; 3957 -5.6; 4353 -5.9; 4788 -6.4; 5267 -6.9; 5793 -9.7; 6373 -10.9; 7010 -8.1; 7711 -10.6; 8482 -14.4; 9330 -14.9; 10263 -11.4; 11289 -9.1; 12418 -10.7; 13660 -11.3; 15026 -6.5; 16529 -5.6; 18182 -7.6; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.72 | 5.4 dB  |
| Peaking | 175 Hz   | 0.71 | -6.9 dB |
| Peaking | 8920 Hz  | 1.99 | -9.3 dB |
| Peaking | 13299 Hz | 3.86 | -5.2 dB |
| Peaking | 19362 Hz | 1.87 | -3.7 dB |
| Peaking | 307 Hz   | 3.28 | -1.1 dB |
| Peaking | 748 Hz   | 1.76 | 1.4 dB  |
| Peaking | 1931 Hz  | 1.7  | -3.8 dB |
| Peaking | 2322 Hz  | 1.42 | 3.6 dB  |
| Peaking | 6100 Hz  | 8.44 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20990%20600%20Ohm/Beyerdynamic%20DT%20990%20600%20Ohm.png)