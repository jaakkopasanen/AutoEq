# Torque t096z Treble Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -1.5; 23 -1.9; 25 -2.3; 28 -2.7; 31 -3.0; 34 -3.2; 37 -3.3; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.2; 79 -5.7; 87 -6.0; 96 -6.3; 106 -6.5; 116 -6.7; 128 -6.8; 141 -7.0; 155 -7.0; 170 -6.9; 187 -6.7; 206 -6.6; 227 -6.2; 249 -5.9; 274 -5.4; 302 -5.0; 332 -4.4; 365 -3.8; 402 -3.2; 442 -2.5; 486 -2.1; 535 -1.5; 588 -0.7; 647 -0.2; 712 0.1; 783 0.5; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.6; 1678 -3.2; 1846 -3.6; 2031 -3.8; 2234 -4.5; 2457 -5.3; 2703 -6.3; 2973 -6.3; 3270 -5.3; 3597 -4.1; 3957 -5.1; 4353 -8.9; 4788 -11.6; 5267 -7.4; 5793 -1.2; 6373 2.0; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -3.5; 11289 -5.8; 12418 -2.8; 13660 -0.3; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Treble Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Treble Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 88 Hz    | 0.45 | -5.2 dB  |
| Peaking | 216 Hz   | 0.92 | -3.9 dB  |
| Peaking | 2666 Hz  | 1.6  | -6.1 dB  |
| Peaking | 4731 Hz  | 5.43 | -11.4 dB |
| Peaking | 11179 Hz | 5.32 | -6.5 dB  |
| Peaking | 384 Hz   | 2.26 | -0.8 dB  |
| Peaking | 802 Hz   | 1.5  | 1.5 dB   |
| Peaking | 1634 Hz  | 3.62 | -1.5 dB  |
| Peaking | 5321 Hz  | 5.02 | -2.7 dB  |
| Peaking | 6555 Hz  | 3.58 | 4.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Treble%20Boost%20Filter/Torque%20t096z%20Treble%20Boost%20Filter.png)