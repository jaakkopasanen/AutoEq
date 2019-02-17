# Polk Audio UltraFit 3000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.8; 25 -15.9; 28 -16.1; 31 -16.2; 34 -16.2; 37 -16.3; 41 -16.4; 45 -16.4; 49 -16.5; 54 -16.7; 60 -16.8; 66 -17.0; 72 -17.2; 79 -17.3; 87 -17.4; 96 -17.5; 106 -17.4; 116 -17.4; 128 -17.3; 141 -17.3; 155 -17.1; 170 -16.8; 187 -16.5; 206 -16.1; 227 -15.6; 249 -15.1; 274 -14.5; 302 -13.9; 332 -13.2; 365 -12.4; 402 -11.7; 442 -11.1; 486 -10.4; 535 -9.7; 588 -9.0; 647 -8.3; 712 -7.8; 783 -7.2; 861 -7.1; 947 -6.9; 1042 -6.4; 1146 -6.4; 1261 -6.8; 1387 -7.3; 1526 -8.0; 1678 -8.3; 1846 -8.2; 2031 -7.9; 2234 -7.2; 2457 -5.8; 2703 -3.9; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.0; 4788 -6.6; 5267 -3.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  1.38 | -8.9 dB |
| Peaking | 52 Hz   |  0.28 | -8.9 dB |
| Peaking | 203 Hz  |  0.57 | -5.6 dB |
| Peaking | 3442 Hz |  3.09 | 7.0 dB  |
| Peaking | 6064 Hz |  4.67 | 6.3 dB  |
| Peaking | 1036 Hz |  1.51 | 1.3 dB  |
| Peaking | 1818 Hz |  1.87 | -2.4 dB |
| Peaking | 2891 Hz |  5.48 | 1.8 dB  |
| Peaking | 4798 Hz | 12.92 | -2.5 dB |
| Peaking | 8238 Hz |  6.11 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000%20sample%20A/Polk%20Audio%20UltraFit%203000%20sample%20A.png)