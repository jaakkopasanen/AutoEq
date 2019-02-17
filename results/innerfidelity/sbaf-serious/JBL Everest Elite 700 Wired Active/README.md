# JBL Everest Elite 700 Wired Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.8; 25 -8.5; 28 -9.2; 31 -9.4; 34 -9.5; 37 -9.4; 41 -9.1; 45 -8.7; 49 -8.1; 54 -7.4; 60 -6.6; 66 -6.1; 72 -5.7; 79 -5.6; 87 -5.7; 96 -6.1; 106 -6.2; 116 -6.1; 128 -5.9; 141 -5.7; 155 -5.8; 170 -6.3; 187 -6.7; 206 -6.2; 227 -5.8; 249 -6.2; 274 -5.8; 302 -5.3; 332 -5.5; 365 -4.9; 402 -4.9; 442 -4.8; 486 -5.6; 535 -5.6; 588 -5.2; 647 -5.4; 712 -5.7; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.3; 1146 -6.1; 1261 -7.4; 1387 -7.5; 1526 -8.3; 1678 -9.1; 1846 -9.8; 2031 -10.6; 2234 -11.2; 2457 -10.7; 2703 -9.2; 2973 -7.4; 3270 -6.2; 3597 -5.6; 3957 -4.4; 4353 -2.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -9.5; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wired Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.93 | -3.5 dB |
| Peaking | 485 Hz  | 0.41 | 1.3 dB  |
| Peaking | 2218 Hz | 1.46 | -5.7 dB |
| Peaking | 5453 Hz | 1.33 | 7.4 dB  |
| Peaking | 8854 Hz | 2.68 | -5.0 dB |
| Peaking | 77 Hz   | 3.52 | 1.2 dB  |
| Peaking | 150 Hz  | 3.06 | 1.3 dB  |
| Peaking | 174 Hz  | 1.85 | -1.2 dB |
| Peaking | 389 Hz  | 5.65 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wired%20Active/JBL%20Everest%20Elite%20700%20Wired%20Active.png)