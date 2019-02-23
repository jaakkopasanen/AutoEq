# AKG Q350 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.5; 25 -8.9; 28 -9.3; 31 -9.7; 34 -10.0; 37 -10.2; 41 -10.5; 45 -10.8; 49 -11.0; 54 -11.3; 60 -11.6; 66 -11.9; 72 -12.1; 79 -12.4; 87 -12.6; 96 -12.9; 106 -13.0; 116 -12.9; 128 -13.0; 141 -12.9; 155 -12.8; 170 -12.5; 187 -12.2; 206 -11.9; 227 -11.3; 249 -11.0; 274 -10.3; 302 -9.7; 332 -9.2; 365 -8.5; 402 -7.8; 442 -6.9; 486 -6.3; 535 -5.5; 588 -4.5; 647 -3.9; 712 -3.4; 783 -2.6; 861 -2.3; 947 -2.2; 1042 -2.0; 1146 -1.8; 1261 -1.5; 1387 -1.5; 1526 -1.9; 1678 -2.0; 1846 -1.5; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -4.2; 3957 -5.6; 4353 -7.5; 4788 -9.3; 5267 -11.7; 5793 -14.4; 6373 -10.0; 7010 -6.2; 7711 -6.2; 8482 -7.5; 9330 -9.5; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q350 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q350 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.35 | -2.9 dB |
| Peaking | 177 Hz  | 0.39 | -4.8 dB |
| Peaking | 988 Hz  | 0.52 | 5.3 dB  |
| Peaking | 2728 Hz | 1.68 | 4.9 dB  |
| Peaking | 5577 Hz | 3.28 | -8.7 dB |
| Peaking | 1025 Hz | 5.43 | -0.2 dB |
| Peaking | 3273 Hz | 7.21 | 2.3 dB  |
| Peaking | 3685 Hz | 2.37 | -1.3 dB |
| Peaking | 7279 Hz | 6.09 | 2.5 dB  |
| Peaking | 9307 Hz | 6.71 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q350%20Quincy%20Jones/AKG%20Q350%20Quincy%20Jones.png)