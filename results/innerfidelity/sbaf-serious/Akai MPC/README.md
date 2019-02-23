# Akai MPC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.9; 25 -5.1; 28 -5.2; 31 -5.3; 34 -5.3; 37 -5.4; 41 -5.4; 45 -5.5; 49 -5.4; 54 -5.4; 60 -5.8; 66 -6.0; 72 -6.2; 79 -6.3; 87 -6.3; 96 -7.0; 106 -8.2; 116 -8.0; 128 -8.0; 141 -8.5; 155 -9.0; 170 -7.9; 187 -8.6; 206 -8.2; 227 -8.1; 249 -7.5; 274 -7.1; 302 -6.8; 332 -6.8; 365 -6.8; 402 -6.8; 442 -6.8; 486 -7.2; 535 -7.1; 588 -6.9; 647 -6.8; 712 -7.3; 783 -7.3; 861 -7.8; 947 -8.2; 1042 -8.5; 1146 -8.6; 1261 -8.7; 1387 -9.5; 1526 -9.0; 1678 -9.5; 1846 -7.9; 2031 -6.5; 2234 -6.6; 2457 -6.8; 2703 -5.6; 2973 -4.7; 3270 -6.9; 3597 -7.6; 3957 -5.9; 4353 -4.9; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Akai MPC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Akai MPC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 81 Hz   | 0.08 | 1.7 dB  |
| Peaking | 156 Hz  | 0.77 | -3.7 dB |
| Peaking | 2572 Hz | 1.38 | 5.8 dB  |
| Peaking | 2623 Hz | 0.41 | -6.1 dB |
| Peaking | 5588 Hz | 1.88 | 9.8 dB  |
| Peaking | 1748 Hz | 7.58 | -1.7 dB |
| Peaking | 1983 Hz | 4.31 | 2.5 dB  |
| Peaking | 2652 Hz | 1.94 | -2.3 dB |
| Peaking | 2893 Hz | 6.42 | 3.4 dB  |
| Peaking | 9606 Hz | 0.16 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Akai%20MPC/Akai%20MPC.png)