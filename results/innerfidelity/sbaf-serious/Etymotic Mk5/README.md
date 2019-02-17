# Etymotic Mk5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -0.9; 66 -1.3; 72 -1.6; 79 -2.0; 87 -2.5; 96 -3.1; 106 -3.4; 116 -3.6; 128 -3.9; 141 -4.1; 155 -4.3; 170 -4.5; 187 -4.7; 206 -4.7; 227 -4.8; 249 -4.9; 274 -4.8; 302 -4.7; 332 -4.7; 365 -4.6; 402 -4.7; 442 -4.5; 486 -4.6; 535 -4.5; 588 -4.3; 647 -4.3; 712 -4.6; 783 -4.7; 861 -5.3; 947 -6.0; 1042 -6.9; 1146 -7.7; 1261 -8.6; 1387 -9.8; 1526 -11.0; 1678 -12.0; 1846 -12.5; 2031 -12.8; 2234 -12.7; 2457 -11.6; 2703 -10.0; 2973 -8.0; 3270 -6.8; 3597 -7.2; 3957 -7.2; 4353 -5.8; 4788 -3.8; 5267 -3.0; 5793 -3.6; 6373 -3.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Mk5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Mk5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.36 | 6.3 dB  |
| Peaking | 651 Hz  | 0.65 | 2.5 dB  |
| Peaking | 1600 Hz | 1.44 | -4.6 dB |
| Peaking | 2215 Hz | 2.22 | -4.6 dB |
| Peaking | 5612 Hz | 2.13 | 4.0 dB  |
| Peaking | 3254 Hz | 7.74 | 1.1 dB  |
| Peaking | 3927 Hz | 7.62 | -1.1 dB |
| Peaking | 6738 Hz | 8.77 | 2.2 dB  |
| Peaking | 7669 Hz | 2.21 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20Mk5/Etymotic%20Mk5.png)