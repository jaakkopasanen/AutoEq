# Beyerdynamic T70p #0002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -1.9; 25 -2.2; 28 -2.5; 31 -2.7; 34 -2.9; 37 -3.1; 41 -3.3; 45 -3.4; 49 -3.5; 54 -3.7; 60 -3.9; 66 -4.1; 72 -4.0; 79 -4.1; 87 -4.6; 96 -5.5; 106 -6.4; 116 -6.9; 128 -7.5; 141 -7.9; 155 -7.9; 170 -7.0; 187 -7.6; 206 -7.3; 227 -6.9; 249 -6.6; 274 -6.6; 302 -7.0; 332 -7.3; 365 -7.7; 402 -8.0; 442 -7.1; 486 -6.6; 535 -6.3; 588 -6.2; 647 -6.4; 712 -6.5; 783 -6.4; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.4; 1387 -6.8; 1526 -7.2; 1678 -7.5; 1846 -7.3; 2031 -5.7; 2234 -3.1; 2457 -1.9; 2703 -2.3; 2973 -3.1; 3270 -3.1; 3597 -2.7; 3957 -0.5; 4353 -4.6; 4788 -4.2; 5267 -1.8; 5793 -0.7; 6373 -3.7; 7010 -8.2; 7711 -13.0; 8482 -15.4; 9330 -15.5; 10263 -12.9; 11289 -8.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70p #0002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70p #0002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.65 | 4.5 dB   |
| Peaking | 3334 Hz  | 1.42 | 4.7 dB   |
| Peaking | 5660 Hz  | 4.03 | 4.0 dB   |
| Peaking | 6120 Hz  | 3.63 | 3.4 dB   |
| Peaking | 8719 Hz  | 2.23 | -11.0 dB |
| Peaking | 147 Hz   | 2.73 | -1.9 dB  |
| Peaking | 384 Hz   | 4.08 | -1.5 dB  |
| Peaking | 1911 Hz  | 1.89 | -2.6 dB  |
| Peaking | 2346 Hz  | 4.32 | 4.0 dB   |
| Peaking | 12206 Hz | 5.05 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70p%20#0002/Beyerdynamic%20T70p%20#0002.png)