# AKG Q460 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.3; 25 -4.0; 28 -4.8; 31 -5.4; 34 -5.8; 37 -6.2; 41 -6.6; 45 -6.9; 49 -7.1; 54 -7.2; 60 -7.5; 66 -7.7; 72 -7.9; 79 -8.1; 87 -8.5; 96 -8.7; 106 -8.9; 116 -9.2; 128 -9.6; 141 -9.9; 155 -10.2; 170 -10.3; 187 -10.6; 206 -10.6; 227 -10.6; 249 -10.8; 274 -10.9; 302 -10.9; 332 -11.1; 365 -11.0; 402 -10.5; 442 -10.3; 486 -10.4; 535 -9.8; 588 -8.1; 647 -6.3; 712 -5.4; 783 -4.3; 861 -5.2; 947 -7.1; 1042 -7.9; 1146 -7.8; 1261 -7.8; 1387 -7.3; 1526 -6.0; 1678 -4.7; 1846 -3.2; 2031 -2.0; 2234 -1.2; 2457 -0.5; 2703 -1.0; 2973 -2.7; 3270 -5.2; 3597 -7.6; 3957 -7.7; 4353 -7.3; 4788 -4.4; 5267 -0.8; 5793 -0.9; 6373 -0.9; 7010 -3.3; 7711 -5.6; 8482 -5.8; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q460 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q460 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.35 | 3.6 dB  |
| Peaking | 233 Hz  | 0.47 | -5.3 dB |
| Peaking | 2520 Hz | 2    | 7.0 dB  |
| Peaking | 4088 Hz | 1.61 | -5.7 dB |
| Peaking | 5524 Hz | 2.4  | 8.0 dB  |
| Peaking | 507 Hz  | 2.37 | -2.1 dB |
| Peaking | 786 Hz  | 1.83 | 5.6 dB  |
| Peaking | 1046 Hz | 1.4  | -3.8 dB |
| Peaking | 1883 Hz | 4.29 | 1.6 dB  |
| Peaking | 8241 Hz | 6.1  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q460%20Quincy%20Jones/AKG%20Q460%20Quincy%20Jones.png)