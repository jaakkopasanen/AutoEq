# NuForce HEM8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -7.0; 28 -7.1; 31 -7.3; 34 -7.4; 37 -7.6; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.7; 66 -9.1; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.6; 106 -10.9; 116 -11.2; 128 -11.5; 141 -11.7; 155 -11.9; 170 -12.1; 187 -12.1; 206 -12.1; 227 -12.0; 249 -12.0; 274 -11.8; 302 -11.6; 332 -11.4; 365 -11.1; 402 -10.8; 442 -10.3; 486 -10.0; 535 -9.5; 588 -8.7; 647 -8.2; 712 -7.7; 783 -7.2; 861 -7.0; 947 -7.3; 1042 -7.8; 1146 -8.1; 1261 -8.3; 1387 -7.7; 1526 -6.2; 1678 -4.0; 1846 -1.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -1.4; 5793 -2.4; 6373 -3.7; 7010 -4.0; 7711 -6.2; 8482 -8.2; 9330 -11.0; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce HEM8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce HEM8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 117 Hz   | 0.59 | -1.9 dB |
| Peaking | 350 Hz   | 0.34 | -5.7 dB |
| Peaking | 1301 Hz  | 1.84 | -6.7 dB |
| Peaking | 2169 Hz  | 0.34 | 8.2 dB  |
| Peaking | 9237 Hz  | 3.11 | -6.9 dB |
| Peaking | 1594 Hz  | 5.87 | -0.8 dB |
| Peaking | 1944 Hz  | 3.76 | 1.3 dB  |
| Peaking | 2890 Hz  | 1.57 | -0.7 dB |
| Peaking | 4523 Hz  | 3.09 | 0.7 dB  |
| Peaking | 14402 Hz | 2.05 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20HEM8/NuForce%20HEM8.png)