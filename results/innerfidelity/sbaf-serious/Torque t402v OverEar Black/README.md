# Torque t402v OverEar Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 -0.2; 25 -0.9; 28 -1.8; 31 -2.5; 34 -3.2; 37 -3.7; 41 -4.4; 45 -4.9; 49 -5.3; 54 -5.8; 60 -6.3; 66 -6.6; 72 -6.8; 79 -7.0; 87 -7.6; 96 -8.5; 106 -9.1; 116 -9.5; 128 -10.0; 141 -10.1; 155 -10.5; 170 -10.1; 187 -10.8; 206 -11.2; 227 -11.4; 249 -11.7; 274 -11.6; 302 -10.9; 332 -9.8; 365 -8.1; 402 -6.1; 442 -3.4; 486 -1.6; 535 0.4; 588 2.8; 647 4.4; 712 5.1; 783 4.7; 861 3.0; 947 1.2; 1042 -0.8; 1146 0.1; 1261 -0.8; 1387 -2.4; 1526 -4.7; 1678 -6.5; 1846 -4.4; 2031 -2.3; 2234 -2.0; 2457 -1.9; 2703 -1.3; 2973 -0.8; 3270 1.3; 3597 2.4; 3957 2.5; 4353 2.4; 4788 2.8; 5267 2.0; 5793 0.1; 6373 -4.2; 7010 -5.3; 7711 -4.9; 8482 -4.9; 9330 -1.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.2; 15026 -0.2; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 127 Hz  | 0.42 | -8.5 dB |
| Peaking | 288 Hz  | 1.13 | -7.0 dB |
| Peaking | 675 Hz  | 1.68 | 8.3 dB  |
| Peaking | 1666 Hz | 3.27 | -6.7 dB |
| Peaking | 7580 Hz | 3.59 | -6.1 dB |
| Peaking | 20 Hz   | 2.57 | 1.8 dB  |
| Peaking | 2764 Hz | 2.52 | -2.0 dB |
| Peaking | 3589 Hz | 2.77 | 2.9 dB  |
| Peaking | 5028 Hz | 2.6  | 3.0 dB  |
| Peaking | 6479 Hz | 6.84 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Black/Torque%20t402v%20OverEar%20Black.png)