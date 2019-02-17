# Sennheiser PX 200 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.2; 60 -1.6; 66 -2.0; 72 -2.3; 79 -2.7; 87 -2.9; 96 -2.1; 106 -2.2; 116 -3.3; 128 -3.6; 141 -3.8; 155 -4.4; 170 -4.7; 187 -5.0; 206 -5.1; 227 -4.6; 249 -4.0; 274 -4.3; 302 -4.9; 332 -4.7; 365 -5.0; 402 -5.3; 442 -5.6; 486 -5.8; 535 -5.9; 588 -5.7; 647 -5.5; 712 -6.0; 783 -6.0; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.7; 1387 -8.8; 1526 -9.0; 1678 -8.4; 1846 -8.9; 2031 -8.6; 2234 -6.9; 2457 -5.6; 2703 -4.0; 2973 -2.3; 3270 -1.3; 3597 -0.9; 3957 -1.0; 4353 -3.6; 4788 -4.1; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.32 | 4.9 dB  |
| Peaking | 81 Hz   | 0.06 | 1.2 dB  |
| Peaking | 1721 Hz | 1.33 | -3.8 dB |
| Peaking | 3406 Hz | 1.94 | 6.2 dB  |
| Peaking | 5965 Hz | 3.95 | 5.9 dB  |
| Peaking | 90 Hz   | 3.03 | -0.7 dB |
| Peaking | 101 Hz  | 6.05 | 1.7 dB  |
| Peaking | 210 Hz  | 2    | -1.1 dB |
| Peaking | 247 Hz  | 3.57 | 1.5 dB  |
| Peaking | 8252 Hz | 4.5  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20200%20II/Sennheiser%20PX%20200%20II.png)