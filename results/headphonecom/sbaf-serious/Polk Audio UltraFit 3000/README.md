# Polk Audio UltraFit 3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.6; 25 -15.7; 28 -15.8; 31 -15.9; 34 -16.0; 37 -16.0; 41 -16.1; 45 -16.1; 49 -16.1; 54 -16.3; 60 -16.4; 66 -16.5; 72 -16.6; 79 -16.7; 87 -16.7; 96 -16.7; 106 -16.6; 116 -16.4; 128 -16.3; 141 -16.1; 155 -15.9; 170 -15.6; 187 -15.2; 206 -14.7; 227 -14.2; 249 -13.6; 274 -13.0; 302 -12.3; 332 -11.6; 365 -10.8; 402 -10.1; 442 -9.5; 486 -8.8; 535 -8.1; 588 -7.4; 647 -6.8; 712 -6.3; 783 -5.8; 861 -5.5; 947 -5.6; 1042 -5.5; 1146 -5.6; 1261 -6.1; 1387 -6.8; 1526 -7.6; 1678 -8.1; 1846 -8.3; 2031 -8.4; 2234 -8.0; 2457 -7.1; 2703 -5.5; 2973 -3.4; 3270 -1.5; 3597 -0.9; 3957 -1.8; 4353 -2.8; 4788 -2.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.24 | -9.4 dB |
| Peaking | 181 Hz  | 0.72 | -4.7 dB |
| Peaking | 3520 Hz | 4.06 | 5.2 dB  |
| Peaking | 5817 Hz | 2.03 | 6.9 dB  |
| Peaking | 7900 Hz | 2.1  | -2.0 dB |
| Peaking | 386 Hz  | 1.46 | -1.0 dB |
| Peaking | 976 Hz  | 0.78 | 2.3 dB  |
| Peaking | 1915 Hz | 1.44 | -3.3 dB |
| Peaking | 3001 Hz | 4.73 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)