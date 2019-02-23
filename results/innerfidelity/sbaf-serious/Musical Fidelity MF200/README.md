# Musical Fidelity MF200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.3; 25 -4.9; 28 -5.7; 31 -6.3; 34 -6.9; 37 -7.3; 41 -7.8; 45 -8.1; 49 -8.4; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.2; 79 -9.3; 87 -9.3; 96 -9.2; 106 -9.5; 116 -9.4; 128 -9.1; 141 -8.7; 155 -8.8; 170 -8.3; 187 -8.0; 206 -7.8; 227 -7.3; 249 -6.9; 274 -6.2; 302 -5.3; 332 -4.8; 365 -4.4; 402 -4.1; 442 -3.4; 486 -2.9; 535 -2.2; 588 -2.2; 647 -3.8; 712 -5.1; 783 -5.7; 861 -6.7; 947 -6.8; 1042 -6.4; 1146 -6.8; 1261 -6.0; 1387 -5.6; 1526 -5.5; 1678 -5.7; 1846 -5.7; 2031 -6.0; 2234 -6.4; 2457 -6.4; 2703 -6.3; 2973 -6.5; 3270 -6.5; 3597 -6.7; 3957 -5.7; 4353 -7.0; 4788 -9.4; 5267 -6.1; 5793 -2.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -6.7; 9330 -6.1; 10263 -5.9; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Musical Fidelity MF200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity MF200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.46 | 3.6 dB  |
| Peaking | 64 Hz   | 0.62 | -2.7 dB |
| Peaking | 134 Hz  | 1.01 | -2.0 dB |
| Peaking | 506 Hz  | 2.12 | 4.1 dB  |
| Peaking | 6331 Hz | 6.98 | 6.3 dB  |
| Peaking | 330 Hz  | 4.82 | 1.0 dB  |
| Peaking | 921 Hz  | 3.83 | -1.5 dB |
| Peaking | 4781 Hz | 6.76 | -3.9 dB |
| Peaking | 5879 Hz | 6.8  | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Musical%20Fidelity%20MF200/Musical%20Fidelity%20MF200.png)