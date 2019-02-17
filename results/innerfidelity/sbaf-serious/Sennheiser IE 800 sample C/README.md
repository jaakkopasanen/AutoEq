# Sennheiser IE 800 sample C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.5; 31 -9.6; 34 -9.7; 37 -9.7; 41 -9.9; 45 -10.0; 49 -10.0; 54 -10.2; 60 -10.3; 66 -10.5; 72 -10.6; 79 -10.8; 87 -11.0; 96 -11.2; 106 -11.1; 116 -11.1; 128 -11.1; 141 -11.0; 155 -10.9; 170 -10.7; 187 -10.4; 206 -10.1; 227 -9.7; 249 -9.5; 274 -9.0; 302 -8.7; 332 -8.3; 365 -7.9; 402 -7.6; 442 -7.1; 486 -6.9; 535 -6.5; 588 -6.0; 647 -5.9; 712 -5.9; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -6.8; 1526 -7.2; 1678 -7.0; 1846 -6.1; 2031 -4.7; 2234 -3.0; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -2.5; 5793 -5.0; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -11.4; 10263 -13.7; 11289 -10.7; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.31 | -3.1 dB |
| Peaking | 150 Hz   | 0.73 | -3.0 dB |
| Peaking | 2677 Hz  | 3.41 | 4.1 dB  |
| Peaking | 4259 Hz  | 1.19 | 6.0 dB  |
| Peaking | 10170 Hz | 3.54 | -8.6 dB |
| Peaking | 685 Hz   | 2.22 | 1.1 dB  |
| Peaking | 1536 Hz  | 2.88 | -1.7 dB |
| Peaking | 5805 Hz  | 7.8  | -2.6 dB |
| Peaking | 6495 Hz  | 8    | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20C/Sennheiser%20IE%20800%20sample%20C.png)