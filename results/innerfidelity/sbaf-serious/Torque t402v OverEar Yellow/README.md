# Torque t402v OverEar Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 -12.8; 23 -13.0; 25 -13.3; 28 -13.6; 31 -13.8; 34 -14.0; 37 -14.1; 41 -14.3; 45 -14.4; 49 -14.5; 54 -14.6; 60 -14.6; 66 -14.7; 72 -14.7; 79 -14.7; 87 -15.4; 96 -16.6; 106 -17.5; 116 -18.1; 128 -18.7; 141 -19.1; 155 -19.1; 170 -18.4; 187 -19.5; 206 -19.3; 227 -18.8; 249 -17.9; 274 -16.5; 302 -14.7; 332 -12.8; 365 -10.4; 402 -8.4; 442 -6.1; 486 -4.4; 535 -2.7; 588 -0.6; 647 1.2; 712 2.9; 783 4.0; 861 3.4; 947 1.6; 1042 -1.4; 1146 -4.1; 1261 -5.2; 1387 -2.9; 1526 -2.5; 1678 -1.1; 1846 -0.6; 2031 -1.5; 2234 -2.8; 2457 -3.1; 2703 -2.7; 2973 -1.4; 3270 0.9; 3597 1.6; 3957 1.9; 4353 0.8; 4788 0.5; 5267 0.2; 5793 -2.1; 6373 -5.7; 7010 -5.0; 7711 -5.3; 8482 -7.2; 9330 -4.9; 10263 -0.0; 11289 0.0; 12418 -0.0; 13660 -3.1; 15026 -2.6; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.29 | -13.3 dB |
| Peaking | 145 Hz   | 0.95 | -11.4 dB |
| Peaking | 258 Hz   | 1.61 | -10.8 dB |
| Peaking | 2382 Hz  | 3.88 | -3.1 dB  |
| Peaking | 8005 Hz  | 2.42 | -7.0 dB  |
| Peaking | 383 Hz   | 2.61 | -2.3 dB  |
| Peaking | 796 Hz   | 1.88 | 6.8 dB   |
| Peaking | 1200 Hz  | 2.9  | -6.3 dB  |
| Peaking | 3880 Hz  | 3.61 | 2.7 dB   |
| Peaking | 14406 Hz | 5.33 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Yellow/Torque%20t402v%20OverEar%20Yellow.png)