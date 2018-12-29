# Audeze iSine20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.8; 116 5.5; 128 5.1; 141 4.8; 155 4.5; 170 4.3; 187 4.1; 206 4.0; 227 3.9; 249 3.7; 274 3.7; 302 3.6; 332 3.5; 365 3.3; 402 3.2; 442 3.2; 486 2.8; 535 2.7; 588 2.6; 647 2.3; 712 1.7; 783 1.4; 861 0.9; 947 0.3; 1042 -0.3; 1146 -0.7; 1261 -0.5; 1387 -0.8; 1526 -2.1; 1678 -1.4; 1846 0.6; 2031 3.0; 2234 5.4; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.05 | 5.9 dB  |
| Peaking | 1614 Hz | 1.84 | -4.8 dB |
| Peaking | 2420 Hz | 1.54 | 6.5 dB  |
| Peaking | 4145 Hz | 1.79 | 4.5 dB  |
| Peaking | 5880 Hz | 3.57 | 4.4 dB  |
| Peaking | 105 Hz  | 0.88 | 1.3 dB  |
| Peaking | 164 Hz  | 0.76 | -1.5 dB |
| Peaking | 583 Hz  | 0.65 | 0.8 dB  |
| Peaking | 1017 Hz | 3.15 | -1.1 dB |
| Peaking | 8337 Hz | 3.83 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20iSine20/Audeze%20iSine20.png)