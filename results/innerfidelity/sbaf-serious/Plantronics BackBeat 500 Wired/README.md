# Plantronics BackBeat 500 Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.8; 31 -8.9; 34 -9.0; 37 -9.0; 41 -8.9; 45 -8.8; 49 -9.0; 54 -9.4; 60 -9.6; 66 -9.7; 72 -9.8; 79 -9.8; 87 -9.6; 96 -9.5; 106 -9.9; 116 -10.5; 128 -11.2; 141 -11.3; 155 -10.9; 170 -10.5; 187 -10.5; 206 -9.9; 227 -9.1; 249 -8.9; 274 -8.9; 302 -8.9; 332 -8.5; 365 -7.8; 402 -6.9; 442 -6.7; 486 -6.8; 535 -6.8; 588 -6.6; 647 -6.9; 712 -7.3; 783 -7.5; 861 -7.4; 947 -6.8; 1042 -6.8; 1146 -6.7; 1261 -6.6; 1387 -7.2; 1526 -8.3; 1678 -9.1; 1846 -9.2; 2031 -8.2; 2234 -7.3; 2457 -5.4; 2703 -4.1; 2973 -3.3; 3270 -2.7; 3597 -2.3; 3957 -1.1; 4353 -0.7; 4788 -0.7; 5267 -0.9; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat 500 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat 500 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.26 | -2.7 dB |
| Peaking | 152 Hz  | 1.32 | -2.9 dB |
| Peaking | 299 Hz  | 2.75 | -1.0 dB |
| Peaking | 1798 Hz | 2.51 | -3.9 dB |
| Peaking | 4597 Hz | 1.19 | 6.3 dB  |
| Peaking | 801 Hz  | 5.3  | -1.1 dB |
| Peaking | 2885 Hz | 3.96 | 0.8 dB  |
| Peaking | 5044 Hz | 3.75 | -0.7 dB |
| Peaking | 6342 Hz | 3.27 | 4.6 dB  |
| Peaking | 7288 Hz | 1.55 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plantronics%20BackBeat%20500%20Wired/Plantronics%20BackBeat%20500%20Wired.png)