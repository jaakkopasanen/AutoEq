# AKG Q350 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.5; 25 -9.8; 28 -10.2; 31 -10.6; 34 -10.9; 37 -11.2; 41 -11.5; 45 -11.7; 49 -12.0; 54 -12.2; 60 -12.5; 66 -12.8; 72 -13.1; 79 -13.3; 87 -13.6; 96 -13.8; 106 -13.9; 116 -13.8; 128 -13.9; 141 -13.9; 155 -13.7; 170 -13.5; 187 -13.1; 206 -12.8; 227 -12.3; 249 -11.9; 274 -11.3; 302 -10.7; 332 -10.1; 365 -9.4; 402 -8.7; 442 -7.8; 486 -7.3; 535 -6.5; 588 -5.5; 647 -4.8; 712 -4.3; 783 -3.6; 861 -3.3; 947 -3.1; 1042 -3.0; 1146 -2.7; 1261 -2.5; 1387 -2.5; 1526 -2.8; 1678 -2.9; 1846 -2.4; 2031 -1.8; 2234 -1.3; 2457 -0.5; 2703 -0.7; 2973 -0.8; 3270 -1.8; 3597 -5.1; 3957 -6.6; 4353 -8.4; 4788 -10.3; 5267 -12.6; 5793 -15.4; 6373 -11.0; 7010 -7.1; 7711 -6.1; 8482 -8.4; 9330 -10.4; 10263 -7.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -6.3; 16529 -4.9; 18182 -3.0; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q350 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q350 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.33 | -8.1 dB  |
| Peaking | 157 Hz   | 0.75 | -5.9 dB  |
| Peaking | 327 Hz   | 1.34 | -3.5 dB  |
| Peaking | 5722 Hz  | 2.37 | -12.1 dB |
| Peaking | 15581 Hz | 3.65 | -4.2 dB  |
| Peaking | 3063 Hz  | 1.3  | 5.5 dB   |
| Peaking | 3945 Hz  | 1.96 | -4.7 dB  |
| Peaking | 7246 Hz  | 3.79 | 2.7 dB   |
| Peaking | 9387 Hz  | 2.85 | -8.3 dB  |
| Peaking | 11173 Hz | 1.98 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.3 dB |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q350%20Quincy%20Jones/AKG%20Q350%20Quincy%20Jones.png)