# Astro A20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.4; 25 -1.9; 28 -2.7; 31 -3.3; 34 -4.0; 37 -4.5; 41 -5.1; 45 -5.6; 49 -6.1; 54 -6.5; 60 -7.0; 66 -7.4; 72 -7.7; 79 -8.0; 87 -8.2; 96 -8.3; 106 -8.3; 116 -8.3; 128 -8.2; 141 -7.9; 155 -7.5; 170 -7.1; 187 -6.6; 206 -6.0; 227 -5.3; 249 -4.6; 274 -4.4; 302 -4.6; 332 -3.3; 365 -2.2; 402 -1.6; 442 -2.5; 486 -3.0; 535 -3.8; 588 -4.3; 647 -3.8; 712 -3.0; 783 -3.3; 861 -3.0; 947 -2.9; 1042 -2.3; 1146 -1.6; 1261 -1.1; 1387 -0.8; 1526 -0.7; 1678 -0.8; 1846 -1.1; 2031 -0.9; 2234 -0.6; 2457 -0.5; 2703 -1.7; 2973 -4.4; 3270 -6.3; 3597 -7.4; 3957 -8.7; 4353 -7.7; 4788 -7.9; 5267 -12.3; 5793 -12.1; 6373 -12.0; 7010 -11.3; 7711 -10.5; 8482 -11.7; 9330 -9.7; 10263 -5.2; 11289 -5.2; 12418 -6.4; 13660 -9.0; 15026 -8.1; 16529 -7.8; 18182 -8.3; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.08 | 4.7 dB  |
| Peaking | 397 Hz   | 3.99 | 3.4 dB  |
| Peaking | 2110 Hz  | 0.67 | 9.0 dB  |
| Peaking | 4429 Hz  | 0.44 | -6.5 dB |
| Peaking | 6263 Hz  | 1.76 | -3.4 dB |
| Peaking | 103 Hz   | 1.04 | -3.5 dB |
| Peaking | 8799 Hz  | 4.77 | -4.7 dB |
| Peaking | 10654 Hz | 1.71 | 4.5 dB  |
| Peaking | 13890 Hz | 3.25 | -2.7 dB |
| Peaking | 18280 Hz | 0.65 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A20/Astro%20A20.png)