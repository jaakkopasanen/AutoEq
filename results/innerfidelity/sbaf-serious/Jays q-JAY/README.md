# Jays q-JAY
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.2; 34 -4.2; 37 -4.3; 41 -4.4; 45 -4.6; 49 -4.7; 54 -4.9; 60 -5.3; 66 -5.6; 72 -5.9; 79 -6.3; 87 -6.7; 96 -7.1; 106 -7.4; 116 -7.6; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.9; 227 -8.8; 249 -8.8; 274 -8.7; 302 -8.6; 332 -8.6; 365 -8.4; 402 -8.2; 442 -7.9; 486 -7.9; 535 -7.6; 588 -7.1; 647 -7.0; 712 -6.9; 783 -6.7; 861 -6.8; 947 -7.1; 1042 -7.4; 1146 -7.5; 1261 -7.6; 1387 -8.1; 1526 -8.4; 1678 -8.4; 1846 -7.9; 2031 -7.4; 2234 -6.7; 2457 -5.4; 2703 -4.0; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -3.9; 4788 -3.4; 5267 -1.6; 5793 -1.2; 6373 -2.6; 7010 -4.3; 7711 -6.5; 8482 -8.4; 9330 -10.4; 10263 -12.4; 11289 -10.8; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays q-JAY GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays q-JAY ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.69 | 3.7 dB  |
| Peaking | 419 Hz   | 0.07 | -1.7 dB |
| Peaking | 3381 Hz  | 2.3  | 7.5 dB  |
| Peaking | 5835 Hz  | 2.52 | 5.7 dB  |
| Peaking | 10208 Hz | 2.91 | -6.5 dB |
| Peaking | 72 Hz    | 1.78 | 0.7 dB  |
| Peaking | 218 Hz   | 0.78 | -0.9 dB |
| Peaking | 752 Hz   | 1.2  | 1.5 dB  |
| Peaking | 1657 Hz  | 2.59 | -1.2 dB |
| Peaking | 12781 Hz | 5.95 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20q-JAY/Jays%20q-JAY.png)