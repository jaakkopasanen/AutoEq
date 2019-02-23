# Etymotic ER-4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -0.8; 79 -1.3; 87 -1.7; 96 -2.0; 106 -2.2; 116 -2.5; 128 -2.8; 141 -3.1; 155 -3.5; 170 -3.7; 187 -3.8; 206 -3.9; 227 -4.0; 249 -4.0; 274 -4.0; 302 -3.9; 332 -3.7; 365 -3.7; 402 -3.8; 442 -3.8; 486 -3.7; 535 -3.8; 588 -3.6; 647 -3.7; 712 -3.8; 783 -4.1; 861 -4.6; 947 -5.5; 1042 -6.4; 1146 -7.4; 1261 -8.4; 1387 -9.6; 1526 -11.0; 1678 -12.2; 1846 -13.6; 2031 -14.7; 2234 -15.0; 2457 -14.3; 2703 -12.4; 2973 -10.1; 3270 -7.9; 3597 -6.8; 3957 -7.7; 4353 -9.1; 4788 -8.5; 5267 -6.1; 5793 -4.1; 6373 -4.4; 7010 -7.0; 7711 -10.1; 8482 -10.0; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -13.4; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.27 | 6.2 dB  |
| Peaking | 593 Hz   | 0.76 | 3.1 dB  |
| Peaking | 2072 Hz  | 1.56 | -9.3 dB |
| Peaking | 16478 Hz | 3.48 | -7.8 dB |
| Peaking | 22050 Hz | 1.91 | -2.1 dB |
| Peaking | 1395 Hz  | 5.54 | -0.7 dB |
| Peaking | 2563 Hz  | 6.97 | -1.4 dB |
| Peaking | 3452 Hz  | 7.07 | 2.1 dB  |
| Peaking | 6092 Hz  | 5.14 | 4.0 dB  |
| Peaking | 8002 Hz  | 4.64 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4S/Etymotic%20ER-4S.png)