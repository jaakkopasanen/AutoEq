# Radius HP-TWF41
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.0; 25 -3.4; 28 -4.0; 31 -4.4; 34 -4.8; 37 -5.1; 41 -5.5; 45 -5.9; 49 -6.2; 54 -6.6; 60 -7.0; 66 -7.5; 72 -7.9; 79 -8.4; 87 -8.8; 96 -9.4; 106 -9.7; 116 -10.0; 128 -10.3; 141 -10.7; 155 -10.9; 170 -11.1; 187 -11.2; 206 -11.3; 227 -11.3; 249 -11.3; 274 -11.2; 302 -11.1; 332 -11.0; 365 -10.8; 402 -10.6; 442 -10.2; 486 -10.0; 535 -9.6; 588 -8.9; 647 -8.5; 712 -7.7; 783 -7.1; 861 -6.8; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -6.2; 1387 -6.3; 1526 -6.4; 1678 -6.3; 1846 -5.9; 2031 -5.5; 2234 -5.1; 2457 -4.4; 2703 -4.1; 2973 -2.6; 3270 -1.4; 3597 -1.1; 3957 -2.0; 4353 -3.5; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -8.5; 10263 -7.9; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -7.3; 16529 -9.6; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-TWF41 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF41 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.64 | 4.6 dB  |
| Peaking | 216 Hz   | 0.49 | -5.2 dB |
| Peaking | 3363 Hz  | 1.85 | 4.7 dB  |
| Peaking | 5931 Hz  | 2.26 | 6.6 dB  |
| Peaking | 8997 Hz  | 1.35 | -2.6 dB |
| Peaking | 505 Hz   | 1.23 | -2.0 dB |
| Peaking | 1287 Hz  | 0.38 | 2.9 dB  |
| Peaking | 1837 Hz  | 0.66 | -2.5 dB |
| Peaking | 4420 Hz  | 9.32 | -1.3 dB |
| Peaking | 16456 Hz | 3.81 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF41/Radius%20HP-TWF41.png)