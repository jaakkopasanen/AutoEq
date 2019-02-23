# Beyerdynamic T5p sn2866
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.4; 25 -4.6; 28 -4.9; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.5; 49 -5.4; 54 -5.3; 60 -5.2; 66 -5.2; 72 -5.0; 79 -4.6; 87 -4.9; 96 -6.1; 106 -8.0; 116 -9.0; 128 -10.1; 141 -10.2; 155 -9.5; 170 -8.2; 187 -9.3; 206 -9.0; 227 -8.4; 249 -7.7; 274 -7.1; 302 -6.5; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.8; 486 -6.2; 535 -6.5; 588 -5.3; 647 -2.3; 712 -4.8; 783 -4.7; 861 -6.4; 947 -6.5; 1042 -5.8; 1146 -7.2; 1261 -9.0; 1387 -7.7; 1526 -9.4; 1678 -9.9; 1846 -9.7; 2031 -9.0; 2234 -10.0; 2457 -7.4; 2703 -5.5; 2973 -4.9; 3270 -3.9; 3597 -2.7; 3957 -0.9; 4353 -4.4; 4788 -0.5; 5267 -1.1; 5793 -5.4; 6373 -5.9; 7010 -4.2; 7711 -7.9; 8482 -11.2; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p sn2866 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sn2866 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 148 Hz   | 2.14 | -3.7 dB |
| Peaking | 659 Hz   | 4.01 | 3.8 dB  |
| Peaking | 1921 Hz  | 1.46 | -4.7 dB |
| Peaking | 4171 Hz  | 1.12 | 5.5 dB  |
| Peaking | 8473 Hz  | 5.09 | -6.1 dB |
| Peaking | 20 Hz    | 1.26 | 2.5 dB  |
| Peaking | 117 Hz   | 0.8  | 4.7 dB  |
| Peaking | 121 Hz   | 2.26 | -5.6 dB |
| Peaking | 207 Hz   | 2.49 | -3.2 dB |
| Peaking | 10027 Hz | 3.82 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sn2866/Beyerdynamic%20T5p%20sn2866.png)