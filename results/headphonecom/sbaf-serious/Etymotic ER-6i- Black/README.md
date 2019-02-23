# Etymotic ER-6i- Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -1.0; 41 -1.2; 45 -1.4; 49 -1.6; 54 -1.9; 60 -2.3; 66 -2.7; 72 -2.9; 79 -3.2; 87 -3.8; 96 -4.1; 106 -4.4; 116 -4.6; 128 -4.9; 141 -5.2; 155 -5.4; 170 -5.6; 187 -5.7; 206 -5.8; 227 -6.1; 249 -6.0; 274 -6.0; 302 -5.8; 332 -5.6; 365 -5.5; 402 -5.8; 442 -5.9; 486 -5.9; 535 -5.7; 588 -5.5; 647 -5.5; 712 -5.5; 783 -5.6; 861 -5.9; 947 -6.6; 1042 -7.3; 1146 -7.9; 1261 -8.7; 1387 -9.6; 1526 -10.6; 1678 -11.4; 1846 -12.0; 2031 -12.4; 2234 -12.3; 2457 -11.4; 2703 -9.9; 2973 -7.8; 3270 -5.5; 3597 -4.1; 3957 -4.7; 4353 -6.4; 4788 -6.5; 5267 -4.2; 5793 -1.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -9.1; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-6i- Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i- Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.35 | 3.4 dB  |
| Peaking | 2057 Hz | 1.54 | -6.6 dB |
| Peaking | 3534 Hz | 4.26 | 4.1 dB  |
| Peaking | 6163 Hz | 4.64 | 6.4 dB  |
| Peaking | 23 Hz   | 0.82 | 2.9 dB  |
| Peaking | 51 Hz   | 1.32 | 0.8 dB  |
| Peaking | 370 Hz  | 3.06 | 0.6 dB  |
| Peaking | 705 Hz  | 2.22 | 1.5 dB  |
| Peaking | 8739 Hz | 7.5  | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i-%20Black/Etymotic%20ER-6i-%20Black.png)