# Philips Fidelio M1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.2; 28 -4.7; 31 -5.1; 34 -5.5; 37 -5.8; 41 -6.1; 45 -6.5; 49 -6.7; 54 -7.0; 60 -7.4; 66 -7.8; 72 -8.2; 79 -8.6; 87 -9.1; 96 -9.4; 106 -9.6; 116 -9.7; 128 -10.1; 141 -10.7; 155 -11.1; 170 -10.7; 187 -10.5; 206 -10.2; 227 -9.3; 249 -8.4; 274 -7.4; 302 -6.7; 332 -6.0; 365 -5.1; 402 -4.7; 442 -4.3; 486 -4.3; 535 -4.4; 588 -4.5; 647 -5.1; 712 -5.8; 783 -6.0; 861 -6.5; 947 -6.9; 1042 -6.8; 1146 -6.1; 1261 -5.1; 1387 -4.7; 1526 -5.6; 1678 -5.2; 1846 -4.7; 2031 -4.7; 2234 -4.3; 2457 -3.7; 2703 -5.2; 2973 -5.4; 3270 -5.4; 3597 -5.9; 3957 -6.0; 4353 -6.2; 4788 -5.2; 5267 -2.2; 5793 -0.5; 6373 -2.8; 7010 -4.2; 7711 -5.6; 8482 -5.8; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -6.1; 18182 -8.7; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.12 | 2.6 dB  |
| Peaking | 140 Hz   | 1.01 | -5.3 dB |
| Peaking | 2315 Hz  | 1.39 | 1.9 dB  |
| Peaking | 4881 Hz  | 1.13 | -2.3 dB |
| Peaking | 5732 Hz  | 3.19 | 7.3 dB  |
| Peaking | 130 Hz   | 1.73 | 3.1 dB  |
| Peaking | 161 Hz   | 0.6  | -2.7 dB |
| Peaking | 428 Hz   | 1.05 | 3.0 dB  |
| Peaking | 938 Hz   | 2.99 | -1.7 dB |
| Peaking | 18870 Hz | 1.52 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1/Philips%20Fidelio%20M1.png)