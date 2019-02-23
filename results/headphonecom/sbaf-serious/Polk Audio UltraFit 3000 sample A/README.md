# Polk Audio UltraFit 3000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.9; 25 -14.9; 28 -15.1; 31 -15.2; 34 -15.2; 37 -15.3; 41 -15.4; 45 -15.4; 49 -15.5; 54 -15.7; 60 -15.8; 66 -16.0; 72 -16.2; 79 -16.3; 87 -16.4; 96 -16.5; 106 -16.4; 116 -16.4; 128 -16.3; 141 -16.3; 155 -16.1; 170 -15.8; 187 -15.5; 206 -15.1; 227 -14.6; 249 -14.1; 274 -13.6; 302 -12.9; 332 -12.2; 365 -11.4; 402 -10.7; 442 -10.1; 486 -9.4; 535 -8.7; 588 -8.0; 647 -7.3; 712 -6.8; 783 -6.2; 861 -6.1; 947 -5.9; 1042 -5.4; 1146 -5.4; 1261 -5.8; 1387 -6.3; 1526 -7.0; 1678 -7.3; 1846 -7.2; 2031 -6.9; 2234 -6.2; 2457 -4.8; 2703 -2.9; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.0; 4788 -5.6; 5267 -2.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.25 | -8.2 dB |
| Peaking | 139 Hz  | 0.72 | -5.2 dB |
| Peaking | 280 Hz  | 1.24 | -3.2 dB |
| Peaking | 3410 Hz | 2.37 | 6.8 dB  |
| Peaking | 6019 Hz | 4.35 | 6.0 dB  |
| Peaking | 1111 Hz | 1.32 | 3.9 dB  |
| Peaking | 1469 Hz | 0.83 | -3.0 dB |
| Peaking | 2836 Hz | 4.87 | 2.0 dB  |
| Peaking | 6745 Hz | 7.21 | 1.6 dB  |
| Peaking | 7732 Hz | 2.86 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000%20sample%20A/Polk%20Audio%20UltraFit%203000%20sample%20A.png)