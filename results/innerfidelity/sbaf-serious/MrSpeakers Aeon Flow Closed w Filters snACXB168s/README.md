# MrSpeakers Aeon Flow Closed w Filters snACXB168s
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.0; 25 -5.1; 28 -5.1; 31 -5.1; 34 -5.1; 37 -5.2; 41 -5.1; 45 -5.1; 49 -5.1; 54 -5.1; 60 -5.0; 66 -4.6; 72 -4.2; 79 -4.0; 87 -4.2; 96 -4.8; 106 -4.9; 116 -4.6; 128 -4.4; 141 -4.4; 155 -4.0; 170 -4.4; 187 -5.1; 206 -5.2; 227 -5.2; 249 -5.5; 274 -5.6; 302 -5.5; 332 -5.5; 365 -5.6; 402 -5.6; 442 -5.6; 486 -5.8; 535 -5.9; 588 -5.6; 647 -5.8; 712 -5.9; 783 -5.5; 861 -5.5; 947 -5.0; 1042 -3.9; 1146 -4.9; 1261 -5.3; 1387 -5.6; 1526 -5.6; 1678 -5.5; 1846 -4.8; 2031 -3.0; 2234 -1.9; 2457 -1.7; 2703 -2.6; 2973 -0.5; 3270 -1.8; 3597 -2.5; 3957 -2.0; 4353 -3.6; 4788 -2.6; 5267 -1.8; 5793 -3.4; 6373 -4.6; 7010 -6.5; 7711 -7.8; 8482 -8.4; 9330 -6.5; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed w Filters snACXB168s GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed w Filters snACXB168s ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 550 Hz  | 0.6  | -1.6 dB |
| Peaking | 1653 Hz | 1.91 | -4.3 dB |
| Peaking | 2168 Hz | 0.84 | 4.1 dB  |
| Peaking | 7041 Hz | 0.81 | 2.7 dB  |
| Peaking | 8024 Hz | 2.11 | -6.9 dB |
| Peaking | 34 Hz   | 1.21 | -0.8 dB |
| Peaking | 159 Hz  | 8.6  | 1.0 dB  |
| Peaking | 4483 Hz | 5.47 | -2.4 dB |
| Peaking | 5057 Hz | 2.5  | 2.4 dB  |
| Peaking | 5925 Hz | 2.94 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20w%20Filters%20snACXB168s/MrSpeakers%20Aeon%20Flow%20Closed%20w%20Filters%20snACXB168s.png)