# SOL Republic Tracks B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.9; 25 -10.5; 28 -11.3; 31 -11.9; 34 -12.5; 37 -12.9; 41 -13.4; 45 -13.6; 49 -13.8; 54 -13.9; 60 -14.0; 66 -14.1; 72 -14.1; 79 -14.0; 87 -13.6; 96 -13.7; 106 -13.8; 116 -13.9; 128 -14.1; 141 -14.1; 155 -14.2; 170 -13.6; 187 -13.7; 206 -13.4; 227 -12.6; 249 -11.4; 274 -9.9; 302 -7.5; 332 -5.2; 365 -2.7; 402 -0.5; 442 -0.5; 486 -1.2; 535 -3.5; 588 -5.1; 647 -6.6; 712 -8.0; 783 -8.4; 861 -8.7; 947 -8.5; 1042 -8.4; 1146 -7.6; 1261 -6.8; 1387 -6.4; 1526 -5.4; 1678 -5.2; 1846 -6.5; 2031 -6.0; 2234 -5.2; 2457 -3.8; 2703 -2.7; 2973 -1.7; 3270 -1.4; 3597 -1.6; 3957 -2.3; 4353 -4.5; 4788 -4.8; 5267 -3.7; 5793 -2.5; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SOL Republic Tracks B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SOL Republic Tracks B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.72 | -4.8 dB |
| Peaking | 242 Hz  | 0.32 | -9.3 dB |
| Peaking | 418 Hz  | 1.46 | 14.9 dB |
| Peaking | 3190 Hz | 1.55 | 5.5 dB  |
| Peaking | 6246 Hz | 4.66 | 4.5 dB  |
| Peaking | 543 Hz  | 3.98 | 1.0 dB  |
| Peaking | 817 Hz  | 2.1  | -1.1 dB |
| Peaking | 1641 Hz | 3.5  | 3.2 dB  |
| Peaking | 1793 Hz | 3.6  | -2.2 dB |
| Peaking | 8328 Hz | 4.18 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 6.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SOL%20Republic%20Tracks%20B/SOL%20Republic%20Tracks%20B.png)