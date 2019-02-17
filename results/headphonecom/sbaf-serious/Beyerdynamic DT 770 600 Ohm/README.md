# Beyerdynamic DT 770 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.9; 41 -3.0; 45 -4.0; 49 -4.9; 54 -4.5; 60 -4.3; 66 -6.3; 72 -7.7; 79 -6.4; 87 -4.0; 96 -6.0; 106 -7.7; 116 -8.7; 128 -9.6; 141 -10.1; 155 -10.2; 170 -9.9; 187 -10.7; 206 -10.5; 227 -10.4; 249 -10.1; 274 -9.9; 302 -9.6; 332 -9.3; 365 -9.0; 402 -8.7; 442 -8.5; 486 -8.1; 535 -7.7; 588 -7.5; 647 -7.3; 712 -6.6; 783 -6.3; 861 -6.5; 947 -6.8; 1042 -6.3; 1146 -5.6; 1261 -5.8; 1387 -6.6; 1526 -7.0; 1678 -7.4; 1846 -7.5; 2031 -7.2; 2234 -7.5; 2457 -8.6; 2703 -7.7; 2973 -5.9; 3270 -3.8; 3597 -1.3; 3957 -1.2; 4353 -3.4; 4788 -0.9; 5267 -10.4; 5793 -13.3; 6373 -12.8; 7010 -9.2; 7711 -11.4; 8482 -15.5; 9330 -14.7; 10263 -8.2; 11289 -6.5; 12418 -8.6; 13660 -9.0; 15026 -6.9; 16529 -8.4; 18182 -12.6; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.64 | 6.3 dB   |
| Peaking | 203 Hz   | 0.75 | -4.4 dB  |
| Peaking | 4589 Hz  | 2.17 | 9.0 dB   |
| Peaking | 5705 Hz  | 3.27 | -11.3 dB |
| Peaking | 8767 Hz  | 3.76 | -9.9 dB  |
| Peaking | 89 Hz    | 9.76 | 3.3 dB   |
| Peaking | 2567 Hz  | 2.47 | -3.3 dB  |
| Peaking | 3780 Hz  | 2.24 | 3.8 dB   |
| Peaking | 4272 Hz  | 8.48 | -5.0 dB  |
| Peaking | 19370 Hz | 0.97 | -8.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%20600%20Ohm/Beyerdynamic%20DT%20770%20600%20Ohm.png)