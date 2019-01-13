# Samsung Level On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -4.8; 23 -5.0; 25 -5.2; 28 -5.4; 31 -5.6; 34 -5.8; 37 -5.9; 41 -6.0; 45 -6.1; 49 -6.2; 54 -6.3; 60 -6.6; 66 -6.7; 72 -6.9; 79 -7.1; 87 -7.4; 96 -7.4; 106 -7.5; 116 -7.9; 128 -8.4; 141 -8.2; 155 -8.2; 170 -7.6; 187 -7.5; 206 -6.9; 227 -6.1; 249 -5.3; 274 -4.2; 302 -3.1; 332 -2.8; 365 -3.0; 402 -3.0; 442 -3.2; 486 -3.3; 535 -3.6; 588 -3.3; 647 -3.0; 712 -2.1; 783 -1.0; 861 -0.9; 947 -0.4; 1042 0.3; 1146 0.8; 1261 1.1; 1387 0.1; 1526 -1.0; 1678 -2.3; 1846 -3.3; 2031 -4.6; 2234 -5.5; 2457 -4.9; 2703 -3.3; 2973 -0.7; 3270 0.1; 3597 -1.1; 3957 -1.0; 4353 0.6; 4788 2.8; 5267 5.2; 5793 5.6; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.54 | -4.2 dB |
| Peaking | 137 Hz   | 0.49 | -7.5 dB |
| Peaking | 2259 Hz  | 2.8  | -6.0 dB |
| Peaking | 5833 Hz  | 3.08 | 6.7 dB  |
| Peaking | 315 Hz   | 3.95 | 1.7 dB  |
| Peaking | 579 Hz   | 2.28 | -2.0 dB |
| Peaking | 1211 Hz  | 2.42 | 2.1 dB  |
| Peaking | 1721 Hz  | 4.18 | -1.2 dB |
| Peaking | 22050 Hz | 1.78 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Samsung%20Level%20On/Samsung%20Level%20On.png)