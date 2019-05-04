# Turtle Beach Recon 50X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.3; 25 -3.5; 28 -3.7; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.2; 45 -4.1; 49 -4.1; 54 -4.1; 60 -4.3; 66 -4.7; 72 -5.1; 79 -5.7; 87 -6.3; 96 -6.7; 106 -7.0; 116 -7.6; 128 -8.3; 141 -9.1; 155 -9.7; 170 -10.1; 187 -10.1; 206 -10.2; 227 -10.5; 249 -10.9; 274 -11.3; 302 -11.2; 332 -11.4; 365 -11.3; 402 -10.5; 442 -10.4; 486 -10.5; 535 -10.5; 588 -10.3; 647 -10.1; 712 -9.3; 783 -8.0; 861 -6.8; 947 -6.2; 1042 -5.9; 1146 -5.8; 1261 -5.6; 1387 -4.8; 1526 -3.9; 1678 -3.4; 1846 -3.3; 2031 -3.4; 2234 -3.2; 2457 -2.8; 2703 -3.2; 2973 -4.4; 3270 -4.5; 3597 -4.3; 3957 -3.7; 4353 -2.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -4.4; 7010 -6.8; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Recon 50X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Recon 50X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.26 | 3.2 dB  |
| Peaking | 255 Hz   | 0.51 | -5.3 dB |
| Peaking | 605 Hz   | 2.6  | -1.9 dB |
| Peaking | 1957 Hz  | 0.88 | 3.6 dB  |
| Peaking | 5139 Hz  | 2.98 | 6.2 dB  |
| Peaking | 350 Hz   | 7.21 | -0.5 dB |
| Peaking | 919 Hz   | 6.45 | 0.8 dB  |
| Peaking | 5963 Hz  | 8.52 | 3.1 dB  |
| Peaking | 6835 Hz  | 2.85 | -2.0 dB |
| Peaking | 20905 Hz | 1.57 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Recon%2050X/Turtle%20Beach%20Recon%2050X.png)