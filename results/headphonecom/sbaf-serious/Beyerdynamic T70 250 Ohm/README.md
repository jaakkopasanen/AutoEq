# Beyerdynamic T70 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.1; 25 -5.3; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.9; 41 -6.0; 45 -6.1; 49 -6.1; 54 -6.3; 60 -6.4; 66 -6.4; 72 -6.5; 79 -6.4; 87 -6.3; 96 -6.7; 106 -7.5; 116 -8.2; 128 -8.8; 141 -9.2; 155 -9.0; 170 -8.0; 187 -8.6; 206 -8.2; 227 -7.5; 249 -7.1; 274 -6.9; 302 -6.9; 332 -7.1; 365 -7.3; 402 -7.7; 442 -8.0; 486 -7.9; 535 -6.4; 588 -6.5; 647 -6.5; 712 -6.5; 783 -6.6; 861 -6.6; 947 -6.6; 1042 -6.4; 1146 -6.4; 1261 -6.4; 1387 -6.8; 1526 -7.1; 1678 -7.1; 1846 -6.2; 2031 -5.3; 2234 -3.8; 2457 -3.3; 2703 -4.0; 2973 -3.9; 3270 -4.2; 3597 -4.4; 3957 -0.5; 4353 -2.3; 4788 -3.3; 5267 -0.6; 5793 -0.5; 6373 -1.3; 7010 -8.4; 7711 -12.7; 8482 -14.5; 9330 -13.7; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 155 Hz   | 1.52 | -2.5 dB  |
| Peaking | 2509 Hz  | 3.29 | 3.1 dB   |
| Peaking | 4032 Hz  | 5.43 | 5.1 dB   |
| Peaking | 5846 Hz  | 2.82 | 8.2 dB   |
| Peaking | 8345 Hz  | 2.64 | -10.2 dB |
| Peaking | 20 Hz    | 0.84 | 1.5 dB   |
| Peaking | 87 Hz    | 3.76 | 0.6 dB   |
| Peaking | 445 Hz   | 4.85 | -1.6 dB  |
| Peaking | 1600 Hz  | 5.5  | -1.2 dB  |
| Peaking | 11067 Hz | 6.34 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)