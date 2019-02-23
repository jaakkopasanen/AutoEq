# Paradigm Shift E1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.9; 25 -12.9; 28 -13.0; 31 -13.2; 34 -13.2; 37 -13.3; 41 -13.4; 45 -13.5; 49 -13.6; 54 -13.8; 60 -14.1; 66 -14.3; 72 -14.6; 79 -14.9; 87 -15.2; 96 -15.6; 106 -15.7; 116 -15.8; 128 -16.0; 141 -16.1; 155 -16.1; 170 -16.0; 187 -15.8; 206 -15.6; 227 -15.2; 249 -14.9; 274 -14.4; 302 -13.8; 332 -13.2; 365 -12.5; 402 -11.8; 442 -10.8; 486 -10.2; 535 -9.4; 588 -8.5; 647 -7.8; 712 -7.5; 783 -6.8; 861 -6.8; 947 -6.8; 1042 -6.9; 1146 -6.5; 1261 -5.4; 1387 -5.2; 1526 -4.6; 1678 -4.3; 1846 -3.1; 2031 -1.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -2.3; 5793 -2.9; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Paradigm Shift E1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.79 | -2.6 dB |
| Peaking | 45 Hz   | 0.22 | -3.3 dB |
| Peaking | 192 Hz  | 0.33 | -7.5 dB |
| Peaking | 620 Hz  | 1.32 | 2.2 dB  |
| Peaking | 3116 Hz | 0.73 | 6.9 dB  |
| Peaking | 1777 Hz | 2.75 | -1.0 dB |
| Peaking | 2117 Hz | 3.68 | 1.7 dB  |
| Peaking | 3041 Hz | 4.89 | -0.8 dB |
| Peaking | 6513 Hz | 5    | 3.1 dB  |
| Peaking | 8074 Hz | 1.93 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E1/Paradigm%20Shift%20E1.png)