# Phiaton Chord MS530 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.7; 28 2.1; 31 1.7; 34 1.3; 37 1.0; 41 0.7; 45 0.5; 49 0.2; 54 -0.0; 60 -0.1; 66 -0.2; 72 -0.5; 79 -0.7; 87 -0.8; 96 -0.8; 106 -0.6; 116 -0.4; 128 -0.2; 141 0.5; 155 0.9; 170 1.2; 187 2.0; 206 1.8; 227 2.0; 249 2.3; 274 2.9; 302 3.3; 332 3.5; 365 3.6; 402 3.4; 442 3.4; 486 3.0; 535 2.8; 588 2.9; 647 2.7; 712 2.2; 783 2.0; 861 1.4; 947 0.7; 1042 -0.3; 1146 -1.0; 1261 -1.5; 1387 -2.3; 1526 -1.4; 1678 -1.0; 1846 -2.4; 2031 -1.0; 2234 0.5; 2457 2.4; 2703 4.4; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.04 | 4.1 dB  |
| Peaking | 103 Hz  | 1.02 | -1.8 dB |
| Peaking | 419 Hz  | 0.45 | 3.8 dB  |
| Peaking | 1631 Hz | 0.97 | -5.3 dB |
| Peaking | 3739 Hz | 0.89 | 7.9 dB  |
| Peaking | 2898 Hz | 4.57 | 1.6 dB  |
| Peaking | 3855 Hz | 3.08 | -0.9 dB |
| Peaking | 6321 Hz | 2.15 | 5.0 dB  |
| Peaking | 7071 Hz | 0.62 | -1.4 dB |
| Peaking | 7514 Hz | 2.66 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530%20Bluetooth/Phiaton%20Chord%20MS530%20Bluetooth.png)