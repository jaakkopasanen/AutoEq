# Philips Fidelio X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.5; 28 -3.9; 31 -5.0; 34 -6.1; 37 -7.1; 41 -8.3; 45 -9.3; 49 -10.2; 54 -11.0; 60 -11.6; 66 -11.9; 72 -12.0; 79 -12.0; 87 -11.9; 96 -11.9; 106 -11.5; 116 -11.0; 128 -10.8; 141 -10.6; 155 -10.3; 170 -9.9; 187 -10.7; 206 -10.2; 227 -9.5; 249 -9.1; 274 -8.7; 302 -8.3; 332 -8.0; 365 -7.6; 402 -7.3; 442 -7.0; 486 -7.0; 535 -6.7; 588 -6.3; 647 -6.2; 712 -6.2; 783 -5.9; 861 -5.4; 947 -4.7; 1042 -4.4; 1146 -4.1; 1261 -4.0; 1387 -5.8; 1526 -7.2; 1678 -7.7; 1846 -7.5; 2031 -7.7; 2234 -7.4; 2457 -7.2; 2703 -5.3; 2973 -3.4; 3270 -5.2; 3597 -6.3; 3957 -6.3; 4353 -7.5; 4788 -7.8; 5267 -7.4; 5793 -8.3; 6373 -6.8; 7010 -6.3; 7711 -8.1; 8482 -10.8; 9330 -10.4; 10263 -5.4; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.99 | 6.1 dB  |
| Peaking | 65 Hz    | 0.65 | -6.9 dB |
| Peaking | 206 Hz   | 0.56 | -3.8 dB |
| Peaking | 1952 Hz  | 2.14 | -3.3 dB |
| Peaking | 8346 Hz  | 1.75 | -5.4 dB |
| Peaking | 1180 Hz  | 5.97 | 1.8 dB  |
| Peaking | 2926 Hz  | 9.85 | 2.8 dB  |
| Peaking | 4656 Hz  | 2.57 | -2.5 dB |
| Peaking | 10736 Hz | 7.62 | 2.1 dB  |
| Peaking | 12379 Hz | 2.88 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -7.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X1/Philips%20Fidelio%20X1.png)