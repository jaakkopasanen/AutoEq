# FLC Technologies FLC8 Bk Gy Bk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.5; 25 -9.7; 28 -9.8; 31 -9.9; 34 -9.9; 37 -9.9; 41 -9.9; 45 -10.0; 49 -10.0; 54 -10.0; 60 -10.0; 66 -10.1; 72 -10.1; 79 -10.2; 87 -10.4; 96 -10.4; 106 -10.4; 116 -10.3; 128 -10.3; 141 -10.2; 155 -10.1; 170 -9.9; 187 -9.7; 206 -9.6; 227 -9.3; 249 -9.1; 274 -8.8; 302 -8.5; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.4; 486 -7.2; 535 -7.0; 588 -6.5; 647 -6.4; 712 -6.5; 783 -6.1; 861 -6.3; 947 -6.9; 1042 -7.5; 1146 -7.8; 1261 -7.9; 1387 -7.9; 1526 -7.5; 1678 -6.8; 1846 -5.7; 2031 -5.0; 2234 -4.8; 2457 -4.4; 2703 -4.6; 2973 -2.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -7.1; 7711 -10.8; 8482 -12.5; 9330 -12.7; 10263 -11.1; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 Bk Gy Bk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 Bk Gy Bk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.4  | -2.8 dB |
| Peaking | 141 Hz   | 0.52 | -3.1 dB |
| Peaking | 3541 Hz  | 2.19 | 5.6 dB  |
| Peaking | 5724 Hz  | 2.05 | 7.4 dB  |
| Peaking | 8569 Hz  | 1.96 | -8.5 dB |
| Peaking | 803 Hz   | 1.52 | 1.6 dB  |
| Peaking | 1268 Hz  | 1.15 | -2.3 dB |
| Peaking | 2032 Hz  | 2.85 | 1.5 dB  |
| Peaking | 10259 Hz | 4.56 | -2.5 dB |
| Peaking | 11471 Hz | 1.92 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk.png)