# Westone UM3X RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.8; 34 -5.0; 37 -5.3; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.3; 60 -6.8; 66 -7.1; 72 -7.4; 79 -7.9; 87 -8.3; 96 -8.8; 106 -9.1; 116 -9.3; 128 -9.6; 141 -9.8; 155 -10.0; 170 -10.1; 187 -10.2; 206 -10.1; 227 -10.0; 249 -10.0; 274 -9.8; 302 -9.6; 332 -9.4; 365 -9.1; 402 -8.8; 442 -8.3; 486 -8.0; 535 -7.6; 588 -6.9; 647 -6.6; 712 -6.5; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.6; 1526 -7.9; 1678 -7.8; 1846 -6.9; 2031 -5.2; 2234 -3.3; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.3  | 3.4 dB  |
| Peaking | 197 Hz   | 0.45 | -4.0 dB |
| Peaking | 1623 Hz  | 1.45 | -6.9 dB |
| Peaking | 3488 Hz  | 0.37 | 8.1 dB  |
| Peaking | 9148 Hz  | 1.25 | -4.6 dB |
| Peaking | 2563 Hz  | 6.36 | 1.6 dB  |
| Peaking | 4706 Hz  | 1    | -1.8 dB |
| Peaking | 6654 Hz  | 1.41 | 3.9 dB  |
| Peaking | 7467 Hz  | 3.81 | -3.9 dB |
| Peaking | 14536 Hz | 1.15 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)