# Phiaton PS 300 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 0.1; 28 -1.8; 31 -3.1; 34 -4.2; 37 -5.0; 41 -5.7; 45 -6.3; 49 -6.8; 54 -7.3; 60 -7.5; 66 -7.4; 72 -8.1; 79 -9.6; 87 -9.8; 96 -10.1; 106 -10.1; 116 -10.2; 128 -10.4; 141 -10.4; 155 -10.6; 170 -10.4; 187 -10.1; 206 -9.6; 227 -9.6; 249 -9.4; 274 -9.5; 302 -9.5; 332 -9.5; 365 -9.0; 402 -7.9; 442 -6.1; 486 -2.6; 535 2.0; 588 4.9; 647 4.3; 712 3.4; 783 2.3; 861 1.2; 947 0.4; 1042 -0.3; 1146 -1.7; 1261 -2.5; 1387 -5.1; 1526 -8.0; 1678 -10.2; 1846 -10.1; 2031 -7.4; 2234 -5.1; 2457 -3.0; 2703 -1.0; 2973 -1.1; 3270 2.5; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.3; 7010 2.5; 7711 0.2; 8482 -1.9; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 300 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 300 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 85 Hz   | 0.69 | -8.9 dB  |
| Peaking | 190 Hz  | 1.36 | -6.6 dB  |
| Peaking | 337 Hz  | 3.04 | -7.4 dB  |
| Peaking | 1796 Hz | 2.68 | -12.0 dB |
| Peaking | 4591 Hz | 1.52 | 7.5 dB   |
| Peaking | 20 Hz   | 3.52 | 5.2 dB   |
| Peaking | 440 Hz  | 3.33 | -5.1 dB  |
| Peaking | 605 Hz  | 2.22 | 7.7 dB   |
| Peaking | 6271 Hz | 5.95 | 2.9 dB   |
| Peaking | 8428 Hz | 3.64 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20300%20NC/Phiaton%20PS%20300%20NC.png)