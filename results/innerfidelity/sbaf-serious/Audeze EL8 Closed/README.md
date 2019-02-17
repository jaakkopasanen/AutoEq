# Audeze EL8 Closed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.2; 25 -4.3; 28 -4.4; 31 -4.4; 34 -4.3; 37 -4.2; 41 -4.2; 45 -4.1; 49 -3.7; 54 -3.4; 60 -4.6; 66 -5.7; 72 -6.0; 79 -6.4; 87 -6.7; 96 -7.2; 106 -7.4; 116 -7.3; 128 -7.0; 141 -6.2; 155 -5.4; 170 -5.0; 187 -4.5; 206 -3.8; 227 -3.3; 249 -3.1; 274 -2.9; 302 -3.0; 332 -3.2; 365 -3.2; 402 -3.5; 442 -3.8; 486 -4.1; 535 -4.2; 588 -4.2; 647 -4.7; 712 -5.2; 783 -5.5; 861 -5.9; 947 -6.2; 1042 -6.4; 1146 -6.5; 1261 -7.0; 1387 -7.5; 1526 -8.3; 1678 -8.9; 1846 -9.0; 2031 -8.4; 2234 -7.6; 2457 -6.6; 2703 -6.4; 2973 -7.1; 3270 -7.6; 3597 -8.1; 3957 -7.8; 4353 -9.1; 4788 -10.9; 5267 -4.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -7.5; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.5; 15026 -9.2; 16529 -7.9; 18182 -6.4; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze EL8 Closed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.01 | 4.0 dB  |
| Peaking | 349 Hz   | 0.58 | 5.7 dB  |
| Peaking | 956 Hz   | 0.04 | -2.2 dB |
| Peaking | 4823 Hz  | 3.94 | -9.6 dB |
| Peaking | 5685 Hz  | 2.02 | 11.2 dB |
| Peaking | 111 Hz   | 3.66 | -1.3 dB |
| Peaking | 1798 Hz  | 2.2  | -4.4 dB |
| Peaking | 1921 Hz  | 1.14 | 3.1 dB  |
| Peaking | 12051 Hz | 1.97 | 2.3 dB  |
| Peaking | 18437 Hz | 0.1  | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Closed/Audeze%20EL8%20Closed.png)