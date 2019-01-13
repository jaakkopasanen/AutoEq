# Brainwavz S1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.2; 28 -9.3; 31 -9.4; 34 -9.5; 37 -9.5; 41 -9.7; 45 -9.8; 49 -9.9; 54 -10.0; 60 -10.1; 66 -10.3; 72 -10.5; 79 -10.7; 87 -10.9; 96 -11.1; 106 -11.1; 116 -11.0; 128 -10.9; 141 -10.8; 155 -10.6; 170 -10.4; 187 -10.0; 206 -9.6; 227 -9.1; 249 -8.6; 274 -8.0; 302 -7.4; 332 -6.7; 365 -6.0; 402 -5.3; 442 -4.5; 486 -3.9; 535 -3.2; 588 -2.3; 647 -1.6; 712 -1.2; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.3; 1261 0.6; 1387 0.3; 1526 -1.0; 1678 -2.7; 1846 -2.9; 2031 -2.6; 2234 -2.5; 2457 -2.0; 2703 -2.1; 2973 -2.0; 3270 -2.3; 3597 -2.9; 3957 -4.3; 4353 -7.3; 4788 -9.0; 5267 -9.4; 5793 -5.3; 6373 -1.4; 7010 0.9; 7711 0.3; 8482 0.0; 9330 -1.2; 10263 -5.2; 11289 -4.3; 12418 -0.8; 13660 -3.9; 15026 -6.3; 16529 -1.1; 18182 0.0; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.22 | -8.7 dB |
| Peaking | 143 Hz   | 0.62 | -6.3 dB |
| Peaking | 305 Hz   | 1.1  | -3.1 dB |
| Peaking | 4823 Hz  | 2.6  | -9.8 dB |
| Peaking | 14633 Hz | 2.26 | -6.0 dB |
| Peaking | 1360 Hz  | 1.43 | 3.6 dB  |
| Peaking | 1753 Hz  | 1.57 | -4.6 dB |
| Peaking | 7256 Hz  | 3.83 | 3.2 dB  |
| Peaking | 10629 Hz | 5.1  | -5.3 dB |
| Peaking | 12641 Hz | 5.6  | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S1/Brainwavz%20S1.png)