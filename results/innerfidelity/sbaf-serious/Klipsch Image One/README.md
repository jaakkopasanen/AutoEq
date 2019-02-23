# Klipsch Image One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -1.5; 60 -2.1; 66 -2.6; 72 -3.3; 79 -4.1; 87 -4.9; 96 -5.7; 106 -6.2; 116 -6.5; 128 -7.1; 141 -7.3; 155 -7.6; 170 -7.6; 187 -7.7; 206 -7.6; 227 -7.3; 249 -7.1; 274 -7.0; 302 -6.9; 332 -6.7; 365 -6.4; 402 -6.2; 442 -5.9; 486 -5.7; 535 -5.2; 588 -4.2; 647 -3.6; 712 -4.0; 783 -3.8; 861 -4.6; 947 -5.2; 1042 -5.5; 1146 -6.1; 1261 -6.8; 1387 -7.4; 1526 -7.8; 1678 -8.3; 1846 -8.8; 2031 -9.1; 2234 -9.5; 2457 -9.6; 2703 -10.4; 2973 -10.4; 3270 -9.3; 3597 -7.1; 3957 -4.4; 4353 -2.8; 4788 -2.3; 5267 -1.8; 5793 -3.9; 6373 -6.4; 7010 -8.1; 7711 -6.3; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.34 | 7.1 dB  |
| Peaking | 126 Hz  | 0.6  | -4.2 dB |
| Peaking | 732 Hz  | 1.27 | 3.4 dB  |
| Peaking | 3386 Hz | 0.72 | -6.7 dB |
| Peaking | 4619 Hz | 1.72 | 10.3 dB |
| Peaking | 4706 Hz | 7.52 | -2.9 dB |
| Peaking | 4964 Hz | 2.41 | 1.8 dB  |
| Peaking | 6789 Hz | 5.93 | -3.3 dB |
| Peaking | 7480 Hz | 2.64 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)