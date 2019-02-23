# Ultimate Ears UE500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.5; 25 -14.4; 28 -14.3; 31 -14.2; 34 -14.0; 37 -13.9; 41 -13.7; 45 -13.6; 49 -13.5; 54 -13.3; 60 -13.2; 66 -13.1; 72 -13.1; 79 -13.0; 87 -13.0; 96 -13.0; 106 -12.8; 116 -12.5; 128 -12.4; 141 -12.2; 155 -11.9; 170 -11.6; 187 -11.2; 206 -10.9; 227 -10.4; 249 -10.0; 274 -9.6; 302 -9.1; 332 -8.6; 365 -8.2; 402 -7.7; 442 -7.1; 486 -6.8; 535 -6.4; 588 -5.7; 647 -5.5; 712 -5.4; 783 -5.0; 861 -5.2; 947 -5.5; 1042 -6.0; 1146 -6.6; 1261 -7.0; 1387 -7.1; 1526 -7.3; 1678 -8.1; 1846 -8.5; 2031 -9.0; 2234 -9.3; 2457 -8.7; 2703 -6.9; 2973 -3.4; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.43 | -7.2 dB |
| Peaking | 120 Hz  | 0.43 | -5.1 dB |
| Peaking | 696 Hz  | 1.29 | 2.2 dB  |
| Peaking | 2231 Hz | 1.6  | -6.3 dB |
| Peaking | 3932 Hz | 1.03 | 8.3 dB  |
| Peaking | 2697 Hz | 6.67 | -1.2 dB |
| Peaking | 3199 Hz | 4.85 | 1.8 dB  |
| Peaking | 4048 Hz | 3.72 | -1.3 dB |
| Peaking | 6237 Hz | 2.79 | 5.3 dB  |
| Peaking | 7175 Hz | 1.63 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)