# Torque t402v OnEar Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.6; 28 -8.9; 31 -9.2; 34 -9.4; 37 -9.6; 41 -9.8; 45 -9.9; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.8; 72 -11.1; 79 -11.2; 87 -11.6; 96 -12.1; 106 -12.5; 116 -12.8; 128 -13.1; 141 -13.3; 155 -13.3; 170 -12.9; 187 -12.9; 206 -12.6; 227 -12.0; 249 -11.4; 274 -10.7; 302 -9.9; 332 -9.4; 365 -8.9; 402 -8.1; 442 -7.2; 486 -6.5; 535 -5.2; 588 -3.3; 647 -1.4; 712 0.5; 783 2.4; 861 2.8; 947 1.5; 1042 -1.2; 1146 -4.1; 1261 -5.5; 1387 -3.9; 1526 -3.2; 1678 -1.8; 1846 -1.2; 2031 -2.0; 2234 -3.2; 2457 -3.6; 2703 -3.3; 2973 -2.5; 3270 -1.1; 3597 -0.7; 3957 -0.8; 4353 -1.9; 4788 -0.5; 5267 4.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.28 | -9.3 dB |
| Peaking | 175 Hz  |  0.82 | -8.4 dB |
| Peaking | 365 Hz  |  1.87 | -4.4 dB |
| Peaking | 2422 Hz |  0.91 | -3.0 dB |
| Peaking | 5945 Hz |  3.81 | 7.5 dB  |
| Peaking | 521 Hz  |  3.36 | -2.4 dB |
| Peaking | 852 Hz  |  2.11 | 6.0 dB  |
| Peaking | 1224 Hz |  2.79 | -5.4 dB |
| Peaking | 1821 Hz |  5.4  | 2.0 dB  |
| Peaking | 4512 Hz | 10.53 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Yellow/Torque%20t402v%20OnEar%20Yellow.png)