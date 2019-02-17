# Etymotic ER-6i- Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.8; 45 -1.0; 49 -1.2; 54 -1.5; 60 -1.9; 66 -2.2; 72 -2.5; 79 -2.8; 87 -3.4; 96 -3.7; 106 -3.9; 116 -4.2; 128 -4.5; 141 -4.8; 155 -5.0; 170 -5.2; 187 -5.3; 206 -5.4; 227 -5.7; 249 -5.6; 274 -5.6; 302 -5.4; 332 -5.2; 365 -5.1; 402 -5.4; 442 -5.5; 486 -5.4; 535 -5.3; 588 -5.1; 647 -5.1; 712 -5.1; 783 -5.2; 861 -5.5; 947 -6.1; 1042 -6.9; 1146 -7.5; 1261 -8.2; 1387 -9.1; 1526 -10.2; 1678 -11.0; 1846 -11.6; 2031 -12.0; 2234 -11.8; 2457 -11.0; 2703 -9.5; 2973 -7.4; 3270 -5.1; 3597 -3.6; 3957 -4.3; 4353 -6.0; 4788 -6.1; 5267 -3.8; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.6; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-6i- Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i- Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.17 | 6.2 dB  |
| Peaking | 2062 Hz | 1.71 | -6.2 dB |
| Peaking | 3558 Hz | 4.39 | 4.1 dB  |
| Peaking | 6142 Hz | 3.58 | 6.4 dB  |
| Peaking | 8661 Hz | 5.41 | -3.1 dB |
| Peaking | 359 Hz  | 3.82 | 0.9 dB  |
| Peaking | 578 Hz  | 2.3  | 1.0 dB  |
| Peaking | 797 Hz  | 2.48 | 1.3 dB  |
| Peaking | 1464 Hz | 3.87 | -1.0 dB |
| Peaking | 9889 Hz | 4.92 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i-%20Black/Etymotic%20ER-6i-%20Black.png)