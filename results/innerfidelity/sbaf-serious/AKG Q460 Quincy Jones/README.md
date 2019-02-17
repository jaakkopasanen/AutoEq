# AKG Q460 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.8; 25 -2.4; 28 -3.2; 31 -3.8; 34 -4.3; 37 -4.7; 41 -5.0; 45 -5.3; 49 -5.5; 54 -5.7; 60 -6.0; 66 -6.2; 72 -6.3; 79 -6.6; 87 -6.9; 96 -7.2; 106 -7.3; 116 -7.7; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.8; 187 -9.1; 206 -9.1; 227 -9.1; 249 -9.3; 274 -9.3; 302 -9.4; 332 -9.6; 365 -9.5; 402 -9.0; 442 -8.8; 486 -8.9; 535 -8.3; 588 -6.6; 647 -4.8; 712 -3.8; 783 -2.8; 861 -3.7; 947 -5.6; 1042 -6.4; 1146 -6.3; 1261 -6.3; 1387 -5.7; 1526 -4.5; 1678 -3.2; 1846 -1.6; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.1; 3270 -3.6; 3597 -6.1; 3957 -6.2; 4353 -5.7; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q460 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q460 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.64 | 8.1 dB  |
| Peaking | 757 Hz  |  1.98 | 7.0 dB  |
| Peaking | 1096 Hz |  0.15 | -4.6 dB |
| Peaking | 2264 Hz |  1.19 | 10.6 dB |
| Peaking | 5784 Hz |  2.56 | 8.1 dB  |
| Peaking | 1868 Hz |  3.56 | 0.9 dB  |
| Peaking | 2303 Hz |  3.16 | -1.4 dB |
| Peaking | 2935 Hz |  3.73 | 2.8 dB  |
| Peaking | 3761 Hz |  2.45 | -2.1 dB |
| Peaking | 5014 Hz | 10.79 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q460%20Quincy%20Jones/AKG%20Q460%20Quincy%20Jones.png)