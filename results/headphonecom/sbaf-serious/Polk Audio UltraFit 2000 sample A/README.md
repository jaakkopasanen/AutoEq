# Polk Audio UltraFit 2000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.5; 54 -3.8; 60 -5.4; 66 -6.6; 72 -7.8; 79 -8.9; 87 -9.8; 96 -10.6; 106 -11.1; 116 -11.3; 128 -11.6; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.0; 206 -10.7; 227 -10.3; 249 -9.9; 274 -9.5; 302 -8.7; 332 -8.1; 365 -7.5; 402 -6.7; 442 -6.6; 486 -6.1; 535 -5.6; 588 -5.0; 647 -4.7; 712 -4.8; 783 -5.6; 861 -7.2; 947 -9.0; 1042 -9.1; 1146 -10.0; 1261 -10.3; 1387 -10.0; 1526 -11.7; 1678 -11.8; 1846 -10.5; 2031 -8.6; 2234 -6.4; 2457 -4.0; 2703 -2.0; 2973 -0.9; 3270 -1.2; 3597 -3.0; 3957 -3.1; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -8.6; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.69 | 7.5 dB  |
| Peaking | 122 Hz  | 0.76 | -6.7 dB |
| Peaking | 1624 Hz | 1.83 | -6.4 dB |
| Peaking | 2920 Hz | 2.15 | 6.1 dB  |
| Peaking | 5374 Hz | 2.3  | 6.4 dB  |
| Peaking | 254 Hz  | 2.21 | -1.2 dB |
| Peaking | 740 Hz  | 1.25 | 4.0 dB  |
| Peaking | 965 Hz  | 2.08 | -4.0 dB |
| Peaking | 6407 Hz | 9.61 | 2.2 dB  |
| Peaking | 9073 Hz | 3.64 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20A/Polk%20Audio%20UltraFit%202000%20sample%20A.png)