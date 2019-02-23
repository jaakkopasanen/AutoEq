# Audeo PFE 121 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.2; 28 -6.4; 31 -6.5; 34 -6.6; 37 -6.7; 41 -6.9; 45 -7.1; 49 -7.2; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.3; 96 -9.5; 106 -9.8; 116 -10.0; 128 -10.2; 141 -10.5; 155 -10.6; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.4; 249 -10.3; 274 -10.0; 302 -9.8; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.1; 647 -6.7; 712 -6.6; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.5; 1387 -6.7; 1526 -7.0; 1678 -6.9; 1846 -6.1; 2031 -5.4; 2234 -4.2; 2457 -2.9; 2703 -3.4; 2973 -3.0; 3270 -2.1; 3597 -1.2; 3957 -0.9; 4353 -1.5; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -10.6; 9330 -10.0; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 121 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 136 Hz  | 0.74 | -3.4 dB |
| Peaking | 287 Hz  | 1.02 | -2.3 dB |
| Peaking | 3536 Hz | 1.39 | 3.8 dB  |
| Peaking | 6038 Hz | 1.45 | 6.3 dB  |
| Peaking | 8578 Hz | 2.43 | -7.2 dB |
| Peaking | 21 Hz   | 1.1  | 0.6 dB  |
| Peaking | 793 Hz  | 3.34 | 0.8 dB  |
| Peaking | 1624 Hz | 2.68 | -1.2 dB |
| Peaking | 2379 Hz | 7.11 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Black%20Filter/Audeo%20PFE%20121%20Black%20Filter.png)