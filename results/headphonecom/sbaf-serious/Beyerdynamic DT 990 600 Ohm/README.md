# Beyerdynamic DT 990 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.1; 34 -1.6; 37 -2.0; 41 -2.6; 45 -3.1; 49 -3.5; 54 -4.1; 60 -4.8; 66 -5.2; 72 -5.0; 79 -5.2; 87 -6.9; 96 -7.8; 106 -8.5; 116 -9.0; 128 -9.4; 141 -9.8; 155 -10.2; 170 -10.1; 187 -10.2; 206 -10.2; 227 -10.0; 249 -9.8; 274 -9.4; 302 -8.9; 332 -8.2; 365 -7.3; 402 -6.6; 442 -5.9; 486 -5.5; 535 -4.8; 588 -4.4; 647 -4.0; 712 -3.6; 783 -3.3; 861 -3.3; 947 -3.8; 1042 -4.0; 1146 -4.4; 1261 -4.4; 1387 -4.7; 1526 -4.9; 1678 -5.0; 1846 -5.3; 2031 -4.9; 2234 -3.5; 2457 -2.7; 2703 -2.7; 2973 -3.5; 3270 -3.8; 3597 -3.5; 3957 -4.0; 4353 -4.3; 4788 -4.8; 5267 -5.3; 5793 -8.1; 6373 -9.3; 7010 -6.5; 7711 -9.0; 8482 -12.8; 9330 -13.3; 10263 -9.8; 11289 -7.5; 12418 -9.1; 13660 -9.7; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.26 | 6.5 dB  |
| Peaking | 175 Hz   | 0.59 | -4.9 dB |
| Peaking | 709 Hz   | 0.89 | 3.7 dB  |
| Peaking | 3044 Hz  | 1.2  | 3.5 dB  |
| Peaking | 9022 Hz  | 2.45 | -7.3 dB |
| Peaking | 5114 Hz  | 4.02 | 1.9 dB  |
| Peaking | 6188 Hz  | 3.57 | -3.5 dB |
| Peaking | 7084 Hz  | 6.51 | 3.3 dB  |
| Peaking | 11030 Hz | 5.56 | 1.6 dB  |
| Peaking | 13182 Hz | 4.46 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20990%20600%20Ohm/Beyerdynamic%20DT%20990%20600%20Ohm.png)