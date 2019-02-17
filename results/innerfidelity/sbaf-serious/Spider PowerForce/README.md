# Spider PowerForce
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.5; 25 -9.1; 28 -10.0; 31 -10.7; 34 -11.3; 37 -11.9; 41 -12.5; 45 -13.0; 49 -13.5; 54 -13.9; 60 -14.4; 66 -14.6; 72 -14.8; 79 -15.1; 87 -15.2; 96 -15.4; 106 -15.4; 116 -15.4; 128 -15.4; 141 -15.4; 155 -15.2; 170 -14.5; 187 -13.9; 206 -12.8; 227 -11.8; 249 -9.5; 274 -8.2; 302 -8.8; 332 -9.1; 365 -9.2; 402 -9.4; 442 -9.6; 486 -9.6; 535 -9.2; 588 -8.5; 647 -7.9; 712 -6.5; 783 -6.7; 861 -6.7; 947 -6.5; 1042 -6.3; 1146 -6.2; 1261 -6.1; 1387 -6.5; 1526 -6.7; 1678 -7.2; 1846 -7.3; 2031 -7.4; 2234 -7.6; 2457 -7.0; 2703 -6.4; 2973 -5.4; 3270 -4.6; 3597 -2.4; 3957 -0.5; 4353 -0.5; 4788 -7.8; 5267 -4.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spider PowerForce GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider PowerForce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 70 Hz    | 0.57 | -7.8 dB  |
| Peaking | 156 Hz   | 1.35 | -5.0 dB  |
| Peaking | 477 Hz   | 2.67 | -2.5 dB  |
| Peaking | 4080 Hz  | 2.61 | 5.9 dB   |
| Peaking | 21440 Hz | 2.58 | 3.1 dB   |
| Peaking | 220 Hz   | 4.43 | -0.9 dB  |
| Peaking | 268 Hz   | 6.58 | 1.9 dB   |
| Peaking | 4977 Hz  | 7.74 | -10.9 dB |
| Peaking | 5319 Hz  | 0.55 | -2.9 dB  |
| Peaking | 5551 Hz  | 1.74 | 9.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20PowerForce/Spider%20PowerForce.png)