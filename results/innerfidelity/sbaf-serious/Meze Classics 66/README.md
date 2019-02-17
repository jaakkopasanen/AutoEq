# Meze Classics 66
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.7; 25 -11.0; 28 -11.5; 31 -11.9; 34 -12.2; 37 -12.3; 41 -12.5; 45 -12.6; 49 -12.7; 54 -12.7; 60 -12.8; 66 -12.9; 72 -13.1; 79 -13.4; 87 -13.6; 96 -13.9; 106 -13.8; 116 -14.1; 128 -14.5; 141 -14.5; 155 -14.9; 170 -14.5; 187 -15.0; 206 -15.2; 227 -15.1; 249 -14.2; 274 -13.0; 302 -13.1; 332 -13.5; 365 -13.3; 402 -12.5; 442 -10.4; 486 -8.8; 535 -6.8; 588 -4.8; 647 -4.3; 712 -5.3; 783 -6.4; 861 -7.5; 947 -7.4; 1042 -5.9; 1146 -3.7; 1261 -1.6; 1387 -1.0; 1526 -1.5; 1678 -1.0; 1846 -0.9; 2031 -1.3; 2234 -1.3; 2457 -1.6; 2703 -4.0; 2973 -3.5; 3270 -0.5; 3597 -3.0; 3957 -2.6; 4353 -0.7; 4788 -0.7; 5267 -1.0; 5793 -0.7; 6373 -1.2; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Classics 66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.34 | -6.0 dB |
| Peaking | 202 Hz  | 1.09 | -5.6 dB |
| Peaking | 366 Hz  | 3.5  | -4.1 dB |
| Peaking | 1763 Hz | 0.99 | 5.9 dB  |
| Peaking | 5100 Hz | 1.69 | 5.8 dB  |
| Peaking | 633 Hz  | 4    | 3.7 dB  |
| Peaking | 938 Hz  | 2.47 | -3.0 dB |
| Peaking | 1271 Hz | 4.7  | 2.3 dB  |
| Peaking | 6407 Hz | 5.06 | 3.1 dB  |
| Peaking | 7663 Hz | 1.84 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2066/Meze%20Classics%2066.png)