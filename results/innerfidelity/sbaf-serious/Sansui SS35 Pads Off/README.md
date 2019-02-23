# Sansui SS35 Pads Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.5; 31 -2.2; 34 -2.9; 37 -3.5; 41 -4.3; 45 -4.9; 49 -5.3; 54 -5.8; 60 -6.5; 66 -7.0; 72 -7.4; 79 -7.7; 87 -8.0; 96 -8.4; 106 -8.3; 116 -8.5; 128 -8.5; 141 -8.6; 155 -8.8; 170 -8.3; 187 -8.2; 206 -7.9; 227 -7.2; 249 -6.7; 274 -6.6; 302 -6.9; 332 -7.8; 365 -8.8; 402 -9.4; 442 -9.6; 486 -9.9; 535 -9.6; 588 -8.6; 647 -8.0; 712 -8.1; 783 -8.4; 861 -9.5; 947 -10.6; 1042 -11.6; 1146 -12.0; 1261 -11.9; 1387 -11.2; 1526 -9.4; 1678 -8.0; 1846 -6.9; 2031 -7.5; 2234 -9.8; 2457 -8.6; 2703 -4.9; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -3.0; 4353 -4.3; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sansui SS35 Pads Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 Pads Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.68 | 6.3 dB  |
| Peaking | 102 Hz  | 0.58 | -2.5 dB |
| Peaking | 1162 Hz | 0.79 | -4.7 dB |
| Peaking | 3296 Hz | 3.27 | 7.3 dB  |
| Peaking | 5674 Hz | 2.75 | 6.6 dB  |
| Peaking | 270 Hz  | 1.89 | 3.0 dB  |
| Peaking | 751 Hz  | 1.44 | 7.0 dB  |
| Peaking | 817 Hz  | 0.47 | -6.1 dB |
| Peaking | 1993 Hz | 1.32 | 6.2 dB  |
| Peaking | 2287 Hz | 4.53 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35%20Pads%20Off/Sansui%20SS35%20Pads%20Off.png)