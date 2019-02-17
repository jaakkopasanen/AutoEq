# Plantronics BackBeat 500 Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.4; 28 -8.5; 31 -8.6; 34 -8.7; 37 -8.7; 41 -8.7; 45 -8.6; 49 -8.7; 54 -9.1; 60 -9.4; 66 -9.5; 72 -9.6; 79 -9.5; 87 -9.3; 96 -9.2; 106 -9.6; 116 -10.2; 128 -10.9; 141 -11.1; 155 -10.6; 170 -10.3; 187 -10.2; 206 -9.7; 227 -8.9; 249 -8.6; 274 -8.6; 302 -8.6; 332 -8.2; 365 -7.6; 402 -6.6; 442 -6.4; 486 -6.6; 535 -6.6; 588 -6.3; 647 -6.6; 712 -7.0; 783 -7.3; 861 -7.2; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -7.0; 1526 -8.0; 1678 -8.9; 1846 -8.9; 2031 -7.9; 2234 -7.0; 2457 -5.2; 2703 -3.8; 2973 -3.1; 3270 -2.5; 3597 -2.1; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat 500 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat 500 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.4  | -2.3 dB |
| Peaking | 152 Hz  | 1.24 | -3.5 dB |
| Peaking | 300 Hz  | 3.78 | -1.1 dB |
| Peaking | 1808 Hz | 2.92 | -3.7 dB |
| Peaking | 4538 Hz | 1.18 | 6.6 dB  |
| Peaking | 2269 Hz | 5.52 | -1.6 dB |
| Peaking | 2560 Hz | 2.6  | 1.4 dB  |
| Peaking | 4782 Hz | 3.13 | -0.6 dB |
| Peaking | 6327 Hz | 3.01 | 4.9 dB  |
| Peaking | 7262 Hz | 1.56 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plantronics%20BackBeat%20500%20Wired/Plantronics%20BackBeat%20500%20Wired.png)