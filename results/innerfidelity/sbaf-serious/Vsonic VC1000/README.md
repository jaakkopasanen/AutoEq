# Vsonic VC1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.0; 25 2.9; 28 2.9; 31 2.8; 34 2.7; 37 2.5; 41 2.3; 45 2.2; 49 2.1; 54 1.9; 60 1.6; 66 1.2; 72 0.8; 79 0.4; 87 -0.1; 96 -0.5; 106 -0.8; 116 -1.0; 128 -1.3; 141 -1.5; 155 -1.8; 170 -2.0; 187 -2.1; 206 -2.2; 227 -2.1; 249 -2.2; 274 -2.1; 302 -2.0; 332 -1.9; 365 -1.7; 402 -1.6; 442 -1.2; 486 -1.2; 535 -0.9; 588 -0.4; 647 -0.1; 712 -0.1; 783 0.3; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.5; 1526 -0.6; 1678 -0.5; 1846 -0.1; 2031 0.5; 2234 0.8; 2457 1.4; 2703 3.0; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 2.8; 4788 2.4; 5267 5.0; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.8; 11289 -4.1; 12418 -1.3; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic VC1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic VC1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  0.38 | 3.1 dB  |
| Peaking | 197 Hz   |  0.56 | -2.6 dB |
| Peaking | 3407 Hz  |  2.45 | 6.6 dB  |
| Peaking | 5945 Hz  |  3.5  | 5.9 dB  |
| Peaking | 11233 Hz |  4.3  | -4.5 dB |
| Peaking | 813 Hz   |  1.4  | 1.4 dB  |
| Peaking | 1361 Hz  |  0.42 | -1.0 dB |
| Peaking | 2921 Hz  |  9.38 | 1.9 dB  |
| Peaking | 4004 Hz  | 14.46 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Vsonic%20VC1000/Vsonic%20VC1000.png)